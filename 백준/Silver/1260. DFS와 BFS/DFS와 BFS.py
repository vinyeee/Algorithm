import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
dfs_chk = [0] * (n+1) # 방문 체크 배열 
bfs_chk = [0] * (n+1)


for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# (1) DFS


def dfs(now):
    dfs_lst=[]
    dfs_chk[now] = 1
    print(now,end=" ")
    for nxt in graph[now]:
        if not dfs_chk[nxt]:
            dfs_chk[nxt] = 1
            dfs(nxt)

#(2) BFS
def bfs(now):
    bfs_chk[now] = 1
    dq = deque()
    dq.append(now)
    while dq:
        now = dq.popleft()
        print(now,end=' ')
        for nxt in graph[now]:
            if not bfs_chk[nxt]:
                bfs_chk[nxt] = 1 #방문했다고 바꿔줌
                dq.append(nxt)      


for i in range(1,n+1): #오름차순으로 정렬 후 dfs bfs 호출
    graph[i].sort()

dfs(v)
print()
bfs(v)