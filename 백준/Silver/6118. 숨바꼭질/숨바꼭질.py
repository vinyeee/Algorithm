import sys
from collections import deque

input = sys.stdin.readline
n,m = map (int,input().split()) #헛간과 길 양방향 

graph = [[] for _ in range(n+1)]
visited = [ -1 for _ in range(n+1)]

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#print(graph)
def bfs(now):
    q = deque()
    q.append(now)
    visited[now] = 0 # 시작 노드는 거리가 0이니까 0
    while q:
        now = q.popleft()
        for nxt in graph[now] :
            if visited[nxt] == -1 :
                q.append(nxt)
                visited[nxt] = visited[now] + 1 #이전에 방문한 순서 + 1 
                         

bfs(1)
#print(visited)
# 숨어야하는 헛간 번호, 그 헛간까지 거리, 그 헛간과 같은 거리를 갖는 헛간 갯수 

num = visited.index(max(visited))
d = visited[num]
x = visited.count(d)

print(num,d,x, end = " ")
