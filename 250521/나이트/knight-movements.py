from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.

graph = [[0] * (n+1) for _ in range((n+1))]
visited = [[0] * (n+1) for _ in range((n+1))]

drs = [-2, -1, 1, 2, 2, 1, -1, -2]
dcs = [1, 2, 2, 1, -1, -2, -2, -1]


q = deque()

def in_range(nr, nc):
    return 0 < nr <= n and 0 < nc <= n 

def can_go(nr, nc):
    return in_range(nr, nc) and not visited[nr][nc]

def bfs():

    while q:
        r,c = q.popleft()
        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr , c + dc
            if can_go(nr, nc) :
                q.append((nr,nc))
                visited[nr][nc] = 1
                graph[nr][nc] = graph[r][c] + 1


    



q.append((r1, c1))
visited[r1][c1] = 1
bfs()

answer = graph[r2][c2]  if visited[r2][c2] != 0 else -1 #  시작점은 방문했으나 움직인 칸수에는 포함되지 않으므로 1을 빼줘야한다
print(answer)  



