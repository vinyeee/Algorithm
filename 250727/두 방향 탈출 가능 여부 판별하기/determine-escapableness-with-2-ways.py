n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0] * n for _ in range(n)]
visited[0][0] = 1
dy = [1,0]
dx = [0,1]

def in_range(y,x):
    return 0 <= y < n and 0 <= x < n

def dfs(y,x):
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(ny,nx) and not visited[ny][nx] and grid[ny][nx]:
            visited[ny][nx] = 1
            dfs(ny,nx)
    

dfs(0,0)

ans = 1 if visited[n-1][n-1] else 0 
print(ans)