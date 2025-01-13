import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())

result = []


def recursion(cnt):
    if cnt == m :
        print(" ".join(list(map(str, result))))
        return
    
    for i in range(1, n + 1):
        result.append(i)
        recursion(cnt + 1)

        
        result.pop()


recursion(0)        
