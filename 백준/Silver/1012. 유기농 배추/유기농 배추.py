import sys
from collections import deque

t = int(sys.stdin.readline())


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,board):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    while dq:
        y,x = dq.popleft()
        for idx in range(4):
            nx = dx[idx] + x #열
            ny = dy[idx] + y #행
            if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 1 and not visited[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = True




for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().split())

    #가로 세로 위치
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    #print(board)
    for i in range(k):
        x,y = map(int, sys.stdin.readline().split())
        board[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i,j,board)
                count += 1
    

    
    #print(board)
    print(count)
