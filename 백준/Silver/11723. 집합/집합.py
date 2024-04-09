import sys

input = sys.stdin.readline
m = int(input()) # 연산의 수 

s = []

for _ in range(m):
    op_n = list(input().split())
    op = op_n[0]
    
    if len(op_n) == 2:
        n = int(op_n[1])
    if op == 'add' and not n in s:
        s.append(n)
    elif op == 'remove' and n in s:
        s.remove(n)
    elif op == 'check':
        if n in s:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if n in s:
            s.remove(n)
        else :
            s.append(n)
    elif op == 'all':
        s = [ i for i in range(1,21)]
    elif op == 'empty':
        s = []
    
