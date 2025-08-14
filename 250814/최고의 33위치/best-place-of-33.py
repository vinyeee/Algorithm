n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_coin = 0 
# 3X3 격자 시작 좌표 
for i in range((n - 3) + 1):
    for j in range((n - 3) + 1):
        coin = 0
        for k in range(i, i+3):
            for l in range(j, j+3):
                if grid[k][l] == 1:
                    coin += 1
        max_coin = max(max_coin, coin)

print(max_coin)