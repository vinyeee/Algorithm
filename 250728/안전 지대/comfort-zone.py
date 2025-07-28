'''
k = 1~100 , 를 가정하고 각각의 상황에서 브루트 포스로 dfs를 돌린다고 가정하면 
k * O(nm) 

1. for문을 돌면서 k = 1 ~ k = 99 를 가정, 비가왔을 때 침수된 지역 h_map 을 구함 
2. h_map 에서 안전영역의 개수를 구하기 위해 dfs
3. 그때의 k와 dfs의 결과를 list 에 저장 safe_zone
4. k의 최댓값과 , 그때의 안전영역의 개수를 print 
'''
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

safe_zone = []

def in_range(y,x):
    return 0 <= y < n and 0 <= x < m 

def can_go(y,x):
    if not in_range(y,x):
        return False
    if h_map[y][x] <= 0 or visited[y][x] == 1 :
        return False
    
    return True

def dfs(y,x):
    visited[y][x] = 1

    dys = [0,1,0,-1]
    dxs = [1,0,-1,0]

    for dy, dx in zip(dys, dxs):
        new_y , new_x = y + dy, x + dx
        if can_go(new_y, new_x):
            dfs(new_y, new_x)



def make_h_map(k):
    h_map = [[0]* m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            h_map[i][j] = grid[i][j] - k
    return h_map 

for k in range(1,100):
    h_map = make_h_map(k)
    visited = [[0] * m for _ in range(n)]

    cnt = 0 
    for i in range(n):
        for j in range(m):
            if can_go(i,j):
                dfs(i,j)
                cnt += 1
    
    safe_zone.append((k,cnt))

# [(1,1), (2,2), (3,3),(4,4)...]
safe_zone.sort(reverse = True, key = lambda x : x[1]) #안전 영역의 수가 큰 순서대로 sort 
print(safe_zone[0][0], safe_zone[0][1])

    
