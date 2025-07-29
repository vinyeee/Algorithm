n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
'''
visited = [[0] * n for _ in range(n)]


dys = [0,1,0,-1]
dxs = [1,-0,-1,0]


def in_range(y,x):
    return 0 <= y < n and 0 <= x < n

def can_go(y,x,block):
    if not in_range(y,x):
        return False
    if visited[y][x] or grid[y][x] != block:
        return False
    return True

def dfs(y,x, block):
    visited[y][x] = 1

    cnt = 1
    for dy, dx in zip(dys, dxs):
        new_y = y + dy
        new_x = x + dx

        if can_go(new_y, new_x,block):
            cnt += dfs(new_y, new_x, block)
    
    return cnt 

ans = []
for i in range(n):
    for j in range(n):
       if can_go(i,j,grid[i][j]):
        block_nums = dfs(i,j,grid[i][j]) #grid[i][j] 는 탐색하고 있는 블록에 적힌 숫자 
        ans.append((grid[i][j], block_nums))



filtered_ans = list(filter(lambda x: x[1] >= 4, ans))
ans.sort(reverse = True, key = lambda x:x[1])

print(len(filtered_ans), ans[0][1])