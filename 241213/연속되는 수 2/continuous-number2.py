n = int(input())

arr = [int(input()) for _ in range(n)]

max_len = 0
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        cnt = 1
        for j in range(i,n-1):
            if arr[j] == arr[j+1]:
                cnt += 1
            else:
                break
    max_len = max(max_len , cnt)

print(max_len)