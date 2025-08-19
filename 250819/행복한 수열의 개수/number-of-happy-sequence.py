n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def is_happy_row(n,m):
    happy_row = 0
    for i in range(n):
        for j in range(n-1):
            max_cnt = 1
            cnt = 1
            if grid[i][j] == grid[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
            if max_cnt >= m:
                happy_row += 1
                break
    return happy_row

def is_happy_col(n,m):
    happy_col = 0
    for j in range(n):
        for i in range(n-1):
            max_cnt = 1
            cnt = 1
            if grid[i][j] == grid[i+1][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
            if max_cnt >= m:
                happy_col += 1
                break
    return happy_col

ans = is_happy_row(n,m) + is_happy_col(n,m)
print(ans)