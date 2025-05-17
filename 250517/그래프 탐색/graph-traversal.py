import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
graph = [[] for _ in range (n + 1)]

for i in range(m):
    u,v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)


cnt = 0 
def dfs(now):
    global cnt 
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = 1
            cnt += 1
            dfs(nxt)
    

visited[1] = 1
dfs(1)

print(cnt)