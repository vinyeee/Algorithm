import sys
input = sys.stdin.readline

r = int(input())
n = int(input())

t = 0
for i in range(n):
    x,y = map(int, input().split())
    t += x * y

if t == r:
    print("Yes")
else:
    print("No")