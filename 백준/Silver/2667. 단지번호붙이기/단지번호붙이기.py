import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

#print(graph)
visited = [[False] * n for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each += 1
    for idx in range(4):
        ny = y + dy[idx]
        nx = x + dx[idx]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx)
                 

result = []
each = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            #방문했다고 바꿔주고
            visited[i][j] = True
            #매 dfs 탐색마다 => 단지 개수 초기화 플러스 
            each = 0
            dfs(i, j)
            #단지 수를 result 배열에 넣음 
            result.append(each)



result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])