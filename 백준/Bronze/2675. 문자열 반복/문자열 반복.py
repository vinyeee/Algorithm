'''
2
3 ABC
5 /HTP
'''

n = int(input())
for i in range(n):
    r_s = input().split() #각 문자를 R번 반복
    R = int(r_s[0])
    S = r_s[1]
    for c in S:
        print(c * R, end = '')
    print()
