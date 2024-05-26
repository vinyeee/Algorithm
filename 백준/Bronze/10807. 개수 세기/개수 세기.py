import sys
input = sys.stdin.readline

n = int(input())
integer_list = list(map(int, input().strip().split()))
v = int(input())

count = 0
for i in range(n):
    if v == integer_list[i]:
        count += 1

print(count)