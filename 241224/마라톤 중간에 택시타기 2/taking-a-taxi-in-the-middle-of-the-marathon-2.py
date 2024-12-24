import sys

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

min_val = sys.maxsize

for i in range(1,n): #건너 뛸 포인트
    x,y = points[0][0] , points[0][1]
    d = 0
    for j in range(1,n):
        if i == j:
            continue
        d += abs(x - points[j][0]) + abs(y - points[j][1])
        x , y = points[j][0] , points[j][1]
    
    min_val = min(min_val, d)
print(min_val)

