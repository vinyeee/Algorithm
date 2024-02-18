import sys

s = int(sys.stdin.readline())

for i in range(1,s+1):
    if i * (i + 1) / 2 == s:
        print(i)
        break
    elif i * (i + 1) / 2 > s:
        print(i-1)
        break