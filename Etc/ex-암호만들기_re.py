from itertools import combinations

L, C = map(int, input().split())  # 암호는 L 자릿수, C개의 암호 풀
password_pool = list(input().split())
result = list()

vowels = ['a', 'e', 'i', 'o', 'u']

possible_list = list(combinations(password_pool, L))
password_pool.sort()

for possible in possible_list:
    vowel_count = 0  # 모음 개수
    for alphabet in possible:
        if alphabet in vowels:
            vowel_count += 1

    consonant_count = L - vowel_count
    if vowel_count >= 1 and consonant_count >= 2:  # 최소 모음 1개, 자음 2개
        result.append(''.join(possible))

for x in result:
    print(x)





