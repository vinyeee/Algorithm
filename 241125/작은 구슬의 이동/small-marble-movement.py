import sys
input = sys.stdin.readline

n, t = map(int, input().split())
r,c,d = map(str, input().split()) # 문자 숫자 섞여있을 땐 str 로 받기
r,c = int(r), int(c)


dr = [0, 1, -1 ,0] #방향을 역방향으로 바꿔줘야 할땐 오른,아래,위,왼
dc = [1, 0, 0, -1]

def in_range(nr,nc):
    return 1<= nr <= n and 1<= nc <= n

direction_mapper = {'R':0,'D':1,'U':2,'L':3}


move_dir = direction_mapper[d] #움직이는 방향

for _ in range(t): #t초 동안 움직임
    nr, nc = r + dr[move_dir] , c + dc[move_dir] #시작 위치에서 d방향에 따라 다음 좌표 결정
    if not in_range(nr, nc):# 다음 좌표가 격자 내에 존재하지 않으면 
        move_dir = 3 - move_dir #방향을 바꿈
    else:
        r,c = nr, nc #이동 
print(r,c)   
