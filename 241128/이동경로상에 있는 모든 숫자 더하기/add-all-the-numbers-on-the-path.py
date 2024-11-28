n, t = map(int, input().split())
cmds = input()

graph = [list(map(int, input().split())) for _ in range(n)]


y, x = n // 2 , n // 2 #시작 위치 

dy = [0 , 1, 0, -1]
dx = [1 , 0, -1, 0]


move_dir = 3

def in_range(ny, nx):
    return 0 <= ny < n and 0 <= nx < n


sum = graph[y][x]

for cmd in cmds:
    if cmd == "R":
        move_dir = ( move_dir + 1 ) % 4

    if cmd ==  "L":
        move_dir = ( move_dir + 3 ) % 4
    else:
        ny, nx = y + dy[move_dir] , x + dx[move_dir]
        if in_range(ny, nx):
            y , x = ny , nx
            sum += graph[ny][nx]

            

print(sum)

            
