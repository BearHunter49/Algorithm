def solution(nums):
    can_max = len(nums) // 2
    total_kind = len(set(nums))

    return min(can_max, total_kind)


print(solution([3,3,3,2,2,2]))  # 2
