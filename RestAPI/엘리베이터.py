import requests
import time

url = 'http://localhost:8000'


def start(user_key, problem_id, number_of_elevators):
    response = requests.post(url + f'/start/{user_key}/{problem_id}/{number_of_elevators}')
    return response.json()


def on_calls(token):
    response = requests.get(url + '/oncalls', headers={'X-Auth-Token': token})
    return response.json()


def action(token, commands):
    response = requests.post(url + '/action', headers={'X-Auth-Token': token}, json={'commands': commands})
    return response.json()


# 명령 하나 폼 만들어서 리턴
def make_command(id, command, call_ids=None):
    if not call_ids:  # 승객 상호작용 X
        return {
            'elevator_id': id,
            'command': command,
        }
    else:
        return {
            'elevator_id': id,
            'command': command,
            'call_ids': call_ids  # 리스트 타입
        }


def is_direction_need(direction, e):
    now = e['floor']

    # 위로 가던 중
    if direction == 'UP':

        # 타고 있는 사람 확인
        for id, floor in e['pushed']:
            diff = now - floor
            if diff < 0:  # 위로 가는 사람 한 명이라도 있음
                return True

        # 예약 확인
        for id, floor in e['reservations']:
            diff = now - floor
            if diff < 0:  # 위로 가는 사람 한 명이라도 있음
                return True

        return False  # 위로 가는 사람 없음

    # 아래로 가던 중
    if direction == 'DOWN':

        # 타고 있는 사람 확인
        for id, floor in e['pushed']:
            diff = now - floor
            if diff > 0:  # 아래로 가는 사람 한 명이라도 있음
                return True

        # 예약 확인
        for id, floor in e['reservations']:
            diff = now - floor
            if diff > 0:  # 아래로 가는 사람 한 명이라도 있음
                return True

        return False  # 아래로 가는 사람 없음


# STOP, OPEN, ENTER, EXIT, CLOSE, UP, DOWN / None or ids
def what_should_do(e, checked_call):
    now = e['floor']
    now_status = e['status']
    now_direction = e['direction']
    now_count = len(e['passengers'])

    # 내리는 사람 우선
    exit_people = list()  # 내려야 하는 사람들 id
    for id, exit_floor in e['pushed']:

        if now == exit_floor:
            if now_status == 'OPENED':  # 이미 열려있으면
                exit_people.append(id)
            elif now_status == 'STOPPED':  # 이미 멈춰있으면
                return 'OPEN', None
            else:  # 이동 중이면
                return 'STOP', None

    if exit_people:  # 현재 내릴 사람 있음
        # 엘리베이터 승객들 내리기
        for id in exit_people:
            e['pushed'].remove((id, now))
        return 'EXIT', exit_people

    # 다음 탈 사람 확인
    enter_people = list()
    fulled_so_remain = list()  # 꽉차서 못탄 사람들
    for id, enter_floor in e['reservations']:

        if now == enter_floor:  # 공간 있어야 함
            if now_count < 8:
                if now_status == 'OPENED':  # 이미 열려있으면
                    enter_people.append(id)
                    now_count += 1
                elif now_status == 'STOPPED':  # 이미 멈춰있으면
                    return 'OPEN', None
                else:  # 이동 중이면
                    return 'STOP', None
            else:
                fulled_so_remain.append(id)

    if enter_people:  # 현재 탈 사람 있음
        # 예약 손님 지우기
        for id in enter_people:
            e['reservations'].remove((id, now))

        # 꽉차서 못 탄 사람 옮기기
        for id in fulled_so_remain:
            e['reservations'].remove((id, now))
            checked_call.remove(id)

        return 'ENTER', enter_people

    # ------- 현재 층과 상호작용 없음--------

    if now_status == 'OPENED':
        return 'CLOSE', None  # 일단 닫기

    if now_status == 'STOPPED':

        if not e['reservations'] and not e['pushed']:  # 할게 없음
            e['direction'] = 'IDLE'
            return 'STOP', None

        if e['reservations'] or e['pushed']:  # 명령이 남아있음

            if now_direction == 'UP':  # 위로 가던 중
                if is_direction_need('UP', e):  # 더 가야함
                    return 'UP', None
                else:  # 위로 갈 사람 없음
                    e['direction'] = 'DOWN'
                    return 'DOWN', None

            if now_direction == 'DOWN':  # 아래로 가던 중
                if is_direction_need('DOWN', e):  # 더 가야함
                    return 'DOWN', None
                else:  # 아래로 갈 사람 없음
                    e['direction'] = 'UP'
                    return 'UP', None

            if now_direction == 'IDLE':  # 멈춰있던 중(새로 사람들이 탄 경우임)
                need_up = 0
                need_down = 0
                for id, floor in e['reservations']:
                    diff = now - floor  # 0인 경우 없음(위에서 걸러짐)
                    # 다수결 투표
                    if diff < 0:
                        need_up += 1
                    else:
                        need_down += 1

                if need_up > need_down:  # 위로 가야함
                    e['direction'] = 'UP'
                    return 'UP', None
                else:  # 아래로 가야함
                    e['direction'] = 'DOWN'
                    return 'DOWN', None

    # 이동 중
    if now_status == 'UPWARD':  # 계속 가면 됨
        if now == 25:  # 유턴
            return 'STOP', None
        return 'UP', None

    if now_status == 'DOWNWARD':  # 계속 가면 됨
        if now == 1:  # 유턴
            return 'UP', None
        return 'DOWN', None


def which_elevator_go(elevator, call_floor):
    possible_list = list()  # (거리, e_id)

    # 수용 인원은 고려 안하기(가는 도중 내릴수도 있으니)
    # 고려하기(STUCK 한다)
    for e_id, e in elevator.items():

        if len(e['passengers']) == 8:  # 가득 찬 엘리베이터
            continue

        # 필요한 방향
        diff = e['floor'] - call_floor
        need_direction = None
        if diff < 0:
            need_direction = 'UP'
        elif diff == 0:
            need_direction = 'NOW'
        else:
            need_direction = 'DOWN'

        if need_direction == 'NOW':  # 같은 층이면
            possible_list.append((0, e_id))
        else:  # 다른 층
            if e['direction'] == 'IDLE':  # 대기 중이면
                possible_list.append((abs(diff), e_id))
            elif need_direction == e['direction']:  # 가는 방향 중에 있으면
                possible_list.append((abs(diff), e_id))

    if not possible_list:  # 조건에 맞는게 하나도 없으면
        return -1
    else:
        possible_list.sort()  # 오름차순 정렬
        return possible_list[0][1]  # 거리가 가장 짧은 e_id


def update_elevator(elevator, api_elevator, elevator_num):
    for i in range(elevator_num):
        elevator[i]['floor'] = api_elevator[i]['floor']
        elevator[i]['passengers'] = api_elevator[i]['passengers']
        elevator[i]['status'] = api_elevator[i]['status']


def apeach_0():
    user_key = 'tester'
    elevator_num = 1

    start_res = start(user_key, 2, elevator_num)
    token = start_res['token']
    # token = 'XbXyo'
    print("my token: ", token)

    # 새로운 엘레베이터 dict
    elevator = dict()  # key: elevator_id, value: stat
    for e in start_res['elevators']:
        elevator[e['id']] = {
            'floor': e['floor'],
            'passengers': e['passengers'],
            'direction': 'IDLE',  # UP, DOWN, IDLE
            'status': e['status'],
            'pushed': [],  # (누가, 몇층에서 내림)
            'reservations': []  # (누가, 몇층에서 누름)
        }

    is_end = start_res['is_end']

    checked_call = list()  # 처리된 손님 id
    checked_end = dict()  # key: call_id, value: end
    while not is_end:  # 완료할 때까지 1가지 timestamp
        calls_res = on_calls(token)  # 상태 불러오기
        print("-------------------------------")
        for ca in calls_res['calls']:
            print(ca['start'], end=', ')
        print()
        for ev in calls_res['elevators']:
            print(f'{ev["id"]}, {ev["floor"]}, {ev["status"]}, {len(ev["passengers"])}')
        # print(calls_res['calls'])


        # 엘레베이터가 각자 태울 손님 선택
        for call in calls_res['calls']:
            call_id = call['id']

            if call_id not in checked_call:  # 아직 예약 안한 손님만
                which = which_elevator_go(elevator, call['start'])  # 어느 엘리베이터가 갈래

                if which != -1:  # 조건에 맞는 엘리베이터 있을 때만
                    elevator[which]['reservations'].append((call_id, call['start']))  # 해당 엘리베이터에 예약 추가
                    checked_call.append(call_id)  # 처리된 call 추가
                    checked_end[call_id] = call['end']  # 목적지 사전 추가

        # Action
        commands = list()
        for e_id, e in elevator.items():
            order, call_ids = what_should_do(e, checked_call)  # STOP, OPEN, ENTER, EXIT, CLOSE, UP, DOWN / None or ids
            commands.append(make_command(e_id, order, call_ids))
            if order == 'ENTER':
                checked_call = list(set(checked_call) - set(call_ids))  # 탄 사람들 처리

                # 타면서 버튼 누르기
                for id in call_ids:
                    e['pushed'].append((id, checked_end[id]))
        print(commands)
        action_res = action(token, commands)  # action 취하기
        is_end = action_res['is_end']  # 결과 확인

        update_elevator(elevator, action_res['elevators'], elevator_num)  # 엘리베이터 dict 업데이트
        # time.sleep(0.05)


if __name__ == '__main__':
    apeach_0()




