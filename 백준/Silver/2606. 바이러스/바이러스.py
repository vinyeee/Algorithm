N = int(input()) #컴퓨터 개수
M = int(input()) #간선 개수

graph = [[] for _ in range(N + 1)]
chk = [0] * (N+1)

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

'''
[2, 5]
[1, 3, 5]
[2]
[7]
[1, 2, 6]
[5]
[4]
'''

cnt = 0
def dfs(now):
    global cnt
    chk[now] = 1
    cnt += 1
    for nxt in graph[now]:
        if not chk[nxt]: #방문한 적이 없으면 
            dfs(nxt) 
    
    return cnt-1


print(dfs(1))
