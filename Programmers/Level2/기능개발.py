from collections import deque
import math


def solution(progresses, speeds):
    answer = []

    progress_queue = deque(progresses)
    speed_queue = deque(speeds)
    completed = 0
    passed_day = 0
    while progress_queue:
        now_progress = progress_queue.popleft()
        now_speed = speed_queue.popleft()

        now_progress += now_speed * passed_day
        if now_progress > 99:
            completed += 1
        else:
            if completed != 0:
                answer.append(completed)
                completed = 0

            passed_day += math.ceil((100 - now_progress) / now_speed)
            completed += 1

    answer.append(completed)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
