import sys
input = sys.stdin.readline

n = int(input())

arr = [ list(map(int,input().split())) for _ in range(n)]

#print(arr)

dxs,dys = [1,0,-1,0],[0,-1,0,1] # 시계방향 



def in_range(ny, nx):
    return 0<= ny < n and 0 <= nx < n

result = 0 

for i in range(n):
    for j in range(n):
        
        y,x = i,j #2차원 배열 순회
        cnt = 0
        for dy, dx in zip(dys,dxs):
            ny , nx = y + dy, x + dx
            if in_range(ny,nx) and arr[ny][nx] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1


print(result)
