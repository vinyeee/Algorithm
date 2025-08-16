import sys
input = sys.stdin.readline

n = int(input().strip())
count = [0] * 10001  # 1~10000 정수라 가정

for _ in range(n):
    num = int(input().strip())
    count[num] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
 