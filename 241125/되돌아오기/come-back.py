import sys
input = sys.stdin.readline


n = int(input())

dy = [0,1,0, -1] #오른, 아래, 왼, 위
dx = [1,0,-1, 0] 


y,x = 0,0
mapper = {'E':0,'S':1,'W':2,'N':3}

ans = -1
cnt = 0 #지금까지 걸린 시간

        
def move(move_dir,l):
    global x,y
    global ans,cnt

    while l > 0: 
        y, x = y + dy[move_dir], x + dx[move_dir]
        cnt += 1
        if y == 0 and x == 0:
            ans = cnt
            return True
        l -= 1
    return False


for _ in range(n):
    d, l = input().split()
    move_dir = mapper[d]
    l = int(l)

    done = move(move_dir,l)
    if done:
        break
    
print(ans)
    
