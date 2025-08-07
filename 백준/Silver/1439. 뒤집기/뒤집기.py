import sys
input = sys.stdin.readline

s = input().strip()


seq_0 = 0
seq_1 = 0 

i = 1
n = len(s)

while i < n:
    if s[i-1] != s[i]: #이전 수와 값이 다르면 
        if s[i-1] == '0':
            seq_0 += 1
        elif s[i-1] == '1':
            seq_1 += 1
    i += 1

if s[-1] == '0':
    seq_0 += 1
else:
    seq_1 += 1
ans = min(seq_0, seq_1)

print(ans)                                       
               