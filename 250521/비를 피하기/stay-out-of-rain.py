from collections import deque
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dys = [0, 1, 0 , -1]
dxs = [1, 0 ,-1, 0]


def in_range(ny, nx):
    return 0<= ny < n and 0 <= nx < n


def can_go(ny, nx):
    return in_range(ny, nx) and not visited[ny][nx] and grid[ny][nx] != 1


def bfs():
    
    while q:
        y,x = q.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if can_go(ny, nx):
                visited[ny][nx] = visited[y][x] + 1
                if grid[ny][nx] == 3:
                    return visited[ny][nx] - 1

                q.append((ny, nx))

    return -1



q = deque()
ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2: # 사람이 서 있던 자리면 
            visited = [[0] * n for _ in range(n)]
            q = deque()
            q.append((i,j)) #시작점을 큐에 넣고 bfs 탐색 시작
            visited[i][j] = 1
            cnt = bfs() #비를 피할 수 있는 최단거리 반환
            ans[i][j] = cnt 
            



for row in ans:
    print(*row)


