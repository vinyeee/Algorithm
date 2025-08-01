'''
못익은게 있으면 -1 , 맨 처음 익은 토마토 0 , 익은 토마토는 익는데 까지 걸리는 시간 , 처음부터 다 익었으면 큐에 들어가면서 다 0으로 세팅   

'''

import sys
input = sys.stdin.readline

m,n = map(int, input().strip().split())
grid = [ list(map(int, input().strip().split())) for _ in range(n)]

visited = [ [-1] * m for _ in range(n)]  #전부 못 익는다고 가정

from collections import deque

for i in range(n): # 토마토가 없는 칸은 -2로 표시 
    for j in range(m):
        if grid[i][j] == -1:
            visited[i][j] = -2


q = deque()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1: #익은 토마토가 있는 위치이면 
            visited[i][j] = 0 #익는데 걸리는 시간 
            q.append((i,j)) #큐에 넣음 


def in_range(y,x):
    return 0 <= y < n and 0 <= x < m

def can_go(y,x):
    if not in_range(y,x): #범위를 벗어나면 False
        return False
    if visited[y][x] >= 0 or grid[y][x] == -1: #이미 방문 했거나 토마토가 없는 자리이면 False 
        return False
    return True


dys = [0,1,0,-1]
dxs = [1,0,-1,0]

while q: 
    y, x = q.popleft()

    for dy, dx in zip(dys, dxs):
        new_y, new_x = y + dy, x + dx 
        
        if can_go(new_y, new_x):
            visited[new_y][new_x] = visited[y][x] + 1
            q.append((new_y, new_x))



#print(visited)

def find_max():
    ans = 0
    for i in range(n):
        if -1 in visited[i]:
            return -1
        ans = max(ans, max(visited[i]))
    return ans
  
print(find_max())
  
       