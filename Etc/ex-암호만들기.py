from itertools import combinations

L, C = map(int, input().split())  # 암호는 L 자릿수, C개의 암호 풀
password_pool = list(input().split())
result = list()

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_pool = list()
consonant_pool = list()

# 자음 모음 분리
for alphabet in password_pool:
    if alphabet in vowels:
        vowel_pool.append(alphabet)
    else:
        consonant_pool.append(alphabet)

vowel_count = len(vowel_pool)
consonant_count = len(consonant_pool)

for i in range(1, vowel_count + 1):
    if (L - i) < 2:  # 자음은 최소 2개
        break

    comb_vowel = list(combinations(vowel_pool, i))
    comb_consonant = list(combinations(consonant_pool, L - i))

    # 모든 조합 구하기
    for vowel in comb_vowel:
        for consonant in comb_consonant:
            temp = list(vowel) + list(consonant)
            temp.sort()  # 알파벳 정렬
            result.append(temp)

for x in result:
    print(''.join(x))








