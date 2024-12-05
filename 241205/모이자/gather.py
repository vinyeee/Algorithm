import sys

INT_MAX = sys.maxsize

n = int(input())
house = list(map(int, input().split()))



#1 2 3 2 6

min_distance = INT_MAX

for i in range(n):
    #i번째 집에 모인다고 가정했을 때 

    move_distance = 0
    for j in range(n):
        move_distance += house[j] * abs(i - j) #j번째 집에 사는 사람 수 - |시작점 - 현재집위치|

    min_distance = min(min_distance, move_distance)

print(min_distance)



