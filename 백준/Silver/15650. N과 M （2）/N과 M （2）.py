import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split()) 
visited = [False] * (n + 1)
result = []

def recursion(cnt):
    if cnt == m:
        print(" ".join(list(map(str, result))))
        return 
    
    for i in range(1,n+1):
        if not visited[i]:
            if len(result) == 0 or (len(result) >0 and i > result[-1]):
                visited[i] = True

                result.append(i)
                recursion(cnt + 1)

                visited[i] = False
                result.pop()


recursion(0)