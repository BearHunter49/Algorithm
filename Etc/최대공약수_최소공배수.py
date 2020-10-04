import math


# 최대공약수 함수
def my_gcd(a, b):  # Greatest Common Divisor
    _pre = max(a, b)
    _post = min(a, b)
    while True:
        r = _pre % _post
        if r == 0:
            return _post
        else:
            _pre = _post
            _post = r


# 최소공배수 함수
def my_lcm(a, b):  # Least Common Multiplier
    return int((a * b) / (math.gcd(a, b)))


# 최대공약수 라이브러리
_gcd = math.gcd(21, 14)


print("math.gcd: ", _gcd)
print("my_gcd: ", my_gcd(22, 14))
print("my_lcm: ", my_lcm(12, 18))

