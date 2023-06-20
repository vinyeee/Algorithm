import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]

cnt = 0
chk = [-1] * (N+1)

for _ in range(M): #간선 개수만큼 받아들임
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(now,depth): #현재 방문 노드, 깊이
    chk[now] = depth # 방문확인 노드에 깊이 저장 
    
    for nxt in graph[now]:
        if(chk[nxt] == -1):
            dfs(nxt,depth + 1)

   


for i in range(1,N+1): #인접 리스트를 정렬
    graph[i].sort()
dfs(R,0)

for i in range(1,N+1):
    print(chk[i])
