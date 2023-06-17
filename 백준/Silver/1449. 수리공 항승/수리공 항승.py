N,L= map(int,input().split())

locations = list(map(int,input().split()))

locations.sort()

cnt = 1
start = locations[0] 
for i in range(1,N):
    if(locations[i] - start + 1 > L ): #테이프로 커버할 수 없는 범위면
        cnt += 1
        start = locations[i]

print(cnt)
