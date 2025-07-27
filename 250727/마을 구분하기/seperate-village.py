n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [ [0] * n for _ in range(n)]
people = []


def in_range(y,x):
    return 0<= y < n and 0 <= x < n

def can_go(y,x):

    if not in_range(y,x): #격자 내에 존재하지 않으면 False
        return False
    if visited[y][x] or grid[y][x] == 0: #방문 했거나 벽이면 False
        return False
    return True 


def dfs(y,x):
    dys = [0,1,0,-1]
    dxs = [1,0,-1,0]    

    cnt = 1

    for dy, dx in zip(dys, dxs):
        new_y , new_x = y + dy , x + dx

        if can_go(new_y, new_x):
            visited[new_y][new_x] = 1
            cnt += dfs(new_y,new_x)
    return cnt 




for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            people.append(dfs(i,j))



people.sort()
print(len(people))
for i in range(len(people)):
    print(people[i])
