import sys
input = sys.stdin.readline

k, n = map(int, input().strip().split())
lans = [ int(input().strip()) for _ in range(k)]


start, end = 1, max(lans)

while start <= end:
    l = (start + end) // 2

    cnt = 0 #몇 개를 만들 수 있는지 
    for lan in lans:
        cnt += (lan // l)

    if n > cnt: #만들어야 하는 랜선 개수가 더 크면 랜선 길이를 더 줄여야 하기 때문에 
        end = l - 1 
    else:
        start = l + 1

    

print(end)     