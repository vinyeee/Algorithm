import sys

m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

d = []
min = 0

for i in range(m,n+1):
    for j in range(1, i+1):
        if j ** 2 == i:
            d.append(i)
            break

sum = sum(d)
if sum == 0:
    print(-1)
else:
    print(sum)
    print(d[0])