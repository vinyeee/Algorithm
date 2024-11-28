n, m = map(int,input().split())
graph = [[' '] * m for _ in range(n)]

y, x = 0, 0 

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

move_dir = 0

graph[y][x] = "A"

def in_range(ny, nx):
    return 0 <= ny <n and 0 <= nx < m

def simulation(y,x):
    global move_dir
    for _ in range (n * m - 1): # 첫 번째 칸을 제외한 나머지 칸을 채우는 횟수 만큼 반복 그러나 이렇게 하게되면 방향전환이 칸을 채우는 횟수에 포함될 수가 있다
        ny, nx = y + dy[move_dir] , x + dx[move_dir]
        if not in_range(ny,nx) or graph[ny][nx] != ' ':
            move_dir = ( move_dir + 1 ) % 4 #따라서 방향전환과 동시에 값을 채워줘야함 
            ny, nx = y + dy[move_dir] , x + dx[move_dir] #방향만 전환하면 안됨 값도 바꿔줘야함 
        ch = chr(ord(graph[y][x]) + 1)
        if ch > "Z":
            ch = "A"
        graph[ny][nx] = ch
        y, x = ny , nx


simulation(y,x)

for row in graph:
    print(" ".join(row))