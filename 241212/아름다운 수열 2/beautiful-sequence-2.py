n,m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

for i in range(n - m + 1):
    copy_b = b[:]
    for j in range(i , i + m):
        if a[j] in copy_b:
            copy_b.remove(a[j])
    if len(copy_b) == 0:
        cnt += 1

print(cnt)