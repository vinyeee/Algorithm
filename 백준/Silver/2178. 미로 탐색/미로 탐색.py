from collections import deque
N,M = map(int, input().split())

adj = [input() for _ in range(N)]
'''
[101111]
[101010]
[101011]
[111011]
'''

#bfs 문제 - 최단거리 
dx = (0,1,0,-1)
dy = (1,0,-1,0)

def isValidate(ny,nx):
    return (0 <= ny < N) and (0 <= nx < M)   # N X M 범위 내에 존재하는지 확인 


def bfs():

    chk=[[False] * M for _ in range(N)]
    chk[0][0] = True
    dq=deque()
    dq.append((0,0,1))
    while dq: #큐에 값이 존재할 때 까지
        y,x,d = dq.popleft() # 행 , 열


        if y == N-1 and x == M-1 :
            return d
        
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if isValidate(ny,nx) and not chk[ny][nx] and adj[ny][nx] == '1': # 범위내에 존재하고 방문하지 않았으며, 갈 수 있는 길이어야함 
                chk[ny][nx] = True
                nd = d + 1 
                dq.append((ny,nx,nd))
                
    



    

print(bfs())
