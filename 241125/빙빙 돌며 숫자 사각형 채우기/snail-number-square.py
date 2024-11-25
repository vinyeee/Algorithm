import sys
input = sys.stdin.readline
#입력
n,m = map(int,input().split()) #행 열

#초기화
graph = [[0] * m for _ in range(n)]

dys = [0, 1, 0, -1] #시계방향 , r, d , l , u #아래 쪽은 y가 음수가 아니라 +1 임을 명심!! 
dxs = [1, 0, -1, 0]

y,x = 0, 0 #시작 위치
move_dir = 0 # 시작 방향
graph[y][x] = 1



#구현 
def in_range(ny,nx):
    return 0<= nx < n and 0 <= ny < m

for i in range(2, n * m + 1): #i 값으로 채울거임
    ny, nx = y + dys[move_dir], x + dxs[move_dir]
    if not in_range(ny,nx) or graph[ny][nx] != 0:
        #격자 바깥이거나 이미 방문했던 곳이라면 90도 회전 
        move_dir = ( move_dir + 1 ) % 4
        
    #한 후 그 다음 위치로 이동한 다음 배열에 값을 채워 넣음 
    y, x = y + dys[move_dir], x + dxs[move_dir]
    graph[y][x] = i



#출력
for i in range(n):
    for j in range(m):
        print(graph[i][j], end = ' ')

    print()


