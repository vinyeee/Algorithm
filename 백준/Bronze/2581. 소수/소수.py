import sys

# 입력을 처리하는 부분
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

decimals = []

# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 주어진 범위 내의 소수를 찾아서 리스트에 추가
for i in range(m, n+1):
    if is_prime(i):
        decimals.append(i)

# 결과 출력
if not decimals:
    print(-1)
else:
    print(sum(decimals))
    print(decimals[0])
