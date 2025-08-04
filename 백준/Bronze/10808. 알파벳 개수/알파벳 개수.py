'''
1) 숫자 하나씩 순회하면서 97랑 차이나는 인덱스에 넣어줌 

'''

import sys
input = sys.stdin.readline

s = input().strip()

ans = [0] * 26

for alpha in s:
    i =  ord(alpha) - 97
    ans[i] += 1

print(*ans) 