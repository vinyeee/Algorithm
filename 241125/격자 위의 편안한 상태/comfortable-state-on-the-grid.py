import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[0] * n for _ in range(n)]

dy = [0, 1, 0, -1] #격자 오른쪽, 아래, 왼쪽, 위 
dx = [1, 0,-1, 0]

def in_range(ny,nx):
    return 0 <= ny < n and 0 <= nx < n

def is_fine(r,c): 
    global graph
    cnt =0 #색이 칠해진 칸
    for i in range(4):
        ny,nx = r + dy[i], c + dx[i] #상하 좌우를 보면서 
        if in_range(ny -1, nx -1) and graph[ny-1][nx -1] == 1: #격자 범위내에 있고 동시에 색이 칠해져있으면
            cnt += 1
    if cnt == 3:
        return True
    else:
        return False  #범위를 벗어나면 false
        #범위를 벗어나지 않으면 
        
        

    

for _ in range(m):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1 #색칠 

    if is_fine(r,c):
        print(1)
    else:
        print(0)