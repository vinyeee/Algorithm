from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
#points = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[0] * n for _ in range(n)]
dxs = [1,0,-1,0]
dys = [0,1,0,-1]

# Please write your code here.

# 시작점이 여러 곳인 경우에 bfs 는 각 시작점에 대해서 bfs를 돌릴 필요 없이
# queue 에다가 처음 시작점 다 때려박고 bfs 한 번 실행해주면 된다. 
# 각 시작점에 대해서 bfs를 다돌려버리면 방문 체크가 까다로움 
q = deque()

def in_range(y,x):
    return 0<= y < n and 0 <= x < n

def can_go(y,x):
    return in_range(y,x) and not visited[y][x] and not grid[y][x] 


def bfs():
    while q:
        y,x = q.popleft()

        for dy, dx in zip(dys,dxs):
            ny, nx = y + dy, x + dx

            if can_go(ny, nx):
                q.append((ny,nx))
                visited[ny][nx] = 1




# queue 에다가 시작점 다 때려 넣기
for _ in range(k):
    y,x = map(int, input().strip().split())
    q.append((y - 1, x - 1))
    visited[y-1][x-1] = 1

#bfs() 시작

bfs()

cnt = sum([
    1
    for i in range(n)
    for j in range(n)
    if visited[i][j]
])

print(cnt)

