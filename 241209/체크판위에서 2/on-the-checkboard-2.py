r,c = map(int, input().split())
arr = [list(input().split()) for _ in range(r)]

cnt = 0

if arr[0][0] == 'W':
    for i in range(1,r-1):
        for j in range(1,c-1):
            if arr[i][j] == 'B':
                for k in range(i+1,r-1):
                    for l in range(j+1,c-1):
                        if arr[k][l] == 'W':
                            cnt += 1
else:
    for i in range(1,n):
        for j in range(1,n):
            if arr[i][j] == 'W':
                for k in range(i+1,n):
                    for l in range(j+1,n):
                        if arr[k][l] == 'B':
                            cnt += 1

print(cnt)