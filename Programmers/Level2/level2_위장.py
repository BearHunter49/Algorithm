def solution(clothes):
    answer = 0

    cloth_dict = dict()
    for cloth, kind in clothes:
        if kind in cloth_dict.keys():
            cloth_dict[kind] += 1
        else:
            cloth_dict[kind] = 1

    temp = 1
    for value in cloth_dict.values():
        temp *= (value + 1)

    answer = temp - 1

    return answer


print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))