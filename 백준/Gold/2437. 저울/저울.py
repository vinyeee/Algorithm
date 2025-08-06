import sys
n = int(input().strip())
s = list(map(int, input().strip().split()))

s.sort()

target = 0 #현재 까지 만들 수 있는 범위 중 가장 큰 수

for weight in s:
    if weight > target + 1: #그 다음 연속한 수를 만들 수 있는지 test 
        print(target + 1)
        break
    target += weight
else:
    print(target + 1)

