import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

h.sort() ## 정렬됐을 때가 가장 시간이 적게 걸림 

s = [0] * n
s[0] = h[0]

for i in range(1,n):
    s[i] = h[i] + s[i-1]

print(sum(s))