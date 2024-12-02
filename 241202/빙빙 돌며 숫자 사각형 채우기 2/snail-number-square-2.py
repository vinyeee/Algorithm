n, m = map(int, input().split())


y , x = 0,0 
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
move_dir = 0 

graph = [[0] * m for _ in range(n)]


graph[y][x] = 1

def in_range(ny , nx) :
    return 0 <= ny < n and 0 <= nx < m

for i in range(2, n * m + 1):
    ny , nx = y + dy[move_dir] , x + dx[move_dir] # 새 좌표 계산해주고 

    if not in_range(ny , nx) or graph[ny][nx] != 0: # 새 좌표로 이동이 가능한지 검사 하고 
        move_dir = ( move_dir + 1 ) % 4 #안되면 방향 전환
    
    y , x = y + dy[move_dir] , x + dx[move_dir] #이동할 방향으로 이동 
    graph[y][x] = i



for i in range(n):
    for j in range(m):
        print(graph[i][j], end = " ")
    print()
