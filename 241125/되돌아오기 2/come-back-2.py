import sys
input = sys.stdin.readline


cmds = input()
#이건 격자가 아님!!
dys = [0,-1,0,1] #오른, 아래, 왼, 위
dxs = [1,0,-1,0]

y,x = 0,0
ans = -1 
move_dir = 3
cnt = 0

def done(cmd):
    global y,x
    global move_dir,cnt,ans
    
    if cmd == "R":
        move_dir = ( move_dir + 1 ) % 4 #각 cmd에 맞게 방향전환 후 
    elif cmd == "L":
        move_dir = ( move_dir + 3 ) % 4
    else:
        y,x = y + dys[move_dir] , x + dxs[move_dir] #이동
    cnt += 1 #움직인 시간 +1
    if y == 0 and x == 0 : #되돌아왔는지 체크 
        ans = cnt
        return True
    else:
        return False


for cmd in cmds:
    if done(cmd):
        break

print(ans)

