n, c, g, h = map(int, input().split())

# n개의 장비들이 선호하는 온도 
arr = [tuple(map(int, input().split())) for _ in range(n)]

max_val = 0
for i in range(1001):
    w = 0
    for j in range(n):
        ta, tb = arr[j][0] , arr[j][1]
        if i > tb:
            w += h
        elif i < ta:
            w += c
        else:
            w += g
    max_val = max(max_val, w)

print(max_val)

