import sys

current = 0
max = 0
for i in range(10):
    x,y = map(int, sys.stdin.readline().split())
    current = current - x + y # 현재 정원
    if current > max:
        max = current


print(max)