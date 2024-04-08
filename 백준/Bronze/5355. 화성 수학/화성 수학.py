import sys
input = sys.stdin.readline

t = int(input())
cases = [ list(input().split()) for _ in range(t)]

for c in cases:
    n = float(c[0])
    for i in range(1,len(c)):
        if c[i] == '@':
            n = n * 3
        elif c[i] == '%':
            n += 5
        else:
            n -= 7
    print("{:.2f}".format(n))