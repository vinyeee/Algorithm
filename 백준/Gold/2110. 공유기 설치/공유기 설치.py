import sys
input = sys.stdin.readline

n, c= map(int, input().strip().split())
Xn = [ int(input().strip()) for _ in range(n)]
Xn.sort()

#처음과 끝은 그 값이 가질 수 있는 최댓값과 최솟값으로 정한다
start, end = 1, Xn[-1] - Xn[0]


while start <= end:
    d = (start + end) // 2

    cnt = 1
    install = Xn[0]

    for i in range(1, n):
        if Xn[i] - install >= d:
            cnt += 1
            install = Xn[i]
    if cnt >= c:
        start = d + 1
    else:
        end = d - 1
    
print(end)