import sys
input = sys.stdin.readline

s = input().strip().split('-')

answer = sum(list(map(int,s[0].split('+'))))

for i in range(1, len(s)):
    elem = sum(list(map(int,s[i].split('+'))))
    answer -= elem

print(answer)
