n = int(input())

arr = [int(input()) for _ in range(n)]

cnt = 0
max_len = 0
for i in range(n):

    if i != 0 and arr[i] == arr[i-1]:
        cnt += 1
    else: 
        cnt = 1
    max_len = max(cnt , max_len)

print(max_len)