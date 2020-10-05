import copy

needed = 0


def my_dfs(now, edges_dict, path):
    if len(path) == needed:  # 경로 다 찾음
        return path

    if now in edges_dict.keys() and edges_dict[now]:  # 다음 경로 존재
        destinations = edges_dict[now]
        length = len(destinations)

        for i in range(length):
            destination = destinations.pop(i)

            tmp = copy.deepcopy(path)
            tmp.append(destination)

            result = my_dfs(destination, edges_dict, tmp)  # 다 찾음
            destinations.insert(i, destination)

            if result:
                return result


def solution(tickets):
    global needed

    needed = len(tickets) + 1
    edges_dict = dict()
    for s, e in tickets:
        if s in edges_dict.keys():
            edges_dict[s].append(e)
        else:
            edges_dict[s] = [e]

    for key in edges_dict.keys():  # 알파벳 순으로 정렬
        edges_dict[key] = list(sorted(edges_dict[key]))

    return my_dfs("ICN", edges_dict, ["ICN"])


print(solution([["ICN", "A"], ["A", "B"], ["B", "C"]]))
