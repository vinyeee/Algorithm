from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = [[-2] * n for _ in range(n)]  # -2: 안 상함, -1: 원래 귤 없던 자리

# 원래 귤 없던 자리 -1 처리
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            ans[i][j] = -1

q = deque()

# 썩은 귤 위치 초기화
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            ans[i][j] = 0
            q.append((i, j))

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

while q:
    y, x = q.popleft()  # popleft 써야 BFS

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if 0 <= ny < n and 0 <= nx < n:
            # 인접 칸이 귤 (1)이고 아직 방문하지 않은 곳(-2)이라면
            if grid[ny][nx] == 1 and ans[ny][nx] == -2:
                ans[ny][nx] = ans[y][x] + 1
                q.append((ny, nx))

# 결과 출력
for i in range(n):
    print(*ans[i])
