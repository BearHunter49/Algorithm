import re

test = "{1,2,3},{2,1},{1,2,4,3},{2}"

result = re.findall(r'\{(.*?)\}', test)
print(result)

# .*: 모든 문자 찾음 (Greedy)
# .*?: 모든 문자 중 가장 먼저 일치하는 경우를 찾음 (Non-Greedy)
