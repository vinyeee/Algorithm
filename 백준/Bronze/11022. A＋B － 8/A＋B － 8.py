import sys
n = int(sys.stdin.readline())

for i in range(n):
    a,b = map(int,input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")