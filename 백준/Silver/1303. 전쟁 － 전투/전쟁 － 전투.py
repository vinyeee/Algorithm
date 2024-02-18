from collections import deque

dx = [-1, 1, 0, 0] #왼, 오 , 아래, 위
dy = [0, 0, -1, 1 ]



def bfs(x, y, color):
    q = deque()
    q.append((x,y)) #시작 정점
    visited[x][y] = True
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:#경계를 벗어나지 않았으면 #x가 행이니까 세로, y가 열이니까 가로보다 작아야함!!  
                if not visited[nx][ny] and war[nx][ny] == color: #방문하지 않았고 아군이면
                    visited[nx][ny] = True #방문했다고 바꿔주고 
                    q.append((nx, ny))#큐에 인접한애들 다 넣기
                    count += 1
    
    return count


n,m = map(int, input().split())

war = []


for _ in range(m): #가로 n, 세로 m
    war.append(list(input()))

visited = [ [False] * n for _ in range(m) ]

blue = 0 
white = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and war[i][j] == 'B':
            blue += bfs(i, j, war[i][j]) ** 2
        elif not visited[i][j] and war[i][j] == 'W':
            white += bfs(i, j, war[i][j]) ** 2

print(white, blue)
