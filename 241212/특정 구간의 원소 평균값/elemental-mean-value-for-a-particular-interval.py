n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i,n):
        sum = 0
        for k in range(i, j+1):
            sum += arr[k]
        mean = sum / (j-i+1) # 구간안에 있는 원소들의 평균값
        sub_arr = arr[i:j+1]
        # print(sub_arr)
        # print(mean)
        if mean in sub_arr:
            cnt += 1
                

print(cnt)