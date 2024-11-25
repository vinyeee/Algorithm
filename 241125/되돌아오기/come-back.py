import sys
input = sys.stdin.readline


n = int(input())

dy = [0,1,0, -1] #오른, 아래, 왼, 위
dx = [1,0,-1, 0] 


y,x = 0,0
mapper = {'E':0,'S':1,'W':2,'N':3}

    
    
def is_return_starting_point(n,y,x):
    cnt = 0 #움직인 횟수 카운트
    for _ in range(n):
        d, l = input().split()
        move_dir = mapper[d]
        l = int(l)
        while l > 0:
            y,x = y + dy[move_dir], x + dx[move_dir]
            cnt += 1
            if y == 0 and x == 0:
                print(cnt)
                return True
            l -= 1 # 한 칸 움직일 때마다 l에서 1씩 빼줌 
    return False


if is_return_starting_point(n,y,x):
    pass
else:
    print(-1) 