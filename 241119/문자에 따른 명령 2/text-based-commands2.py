import sys
input = sys.stdin.readline

cmds = input()
x,y = 0, 0 

# 동 남 서 북 (시계 방향 순으로 dx, dy) 를 정의 
dir_num = 3 # 지금 일단 북쪽을 보고 있음 

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for cmd in cmds:
    if cmd == "L":
        dir_num = ( dir_num -1 + 4 ) % 4
    elif cmd == "R":
        dir_num = ( dir_num + 1 ) % 4
    else:
        x,y = x+dx[dir_num], y+dy[dir_num]

print(x,y)