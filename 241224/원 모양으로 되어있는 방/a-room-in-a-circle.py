import sys
n = int(input())
people = [int(input()) for _ in range(n)]


min_val = sys.maxsize


for i in range(n): #시작하는 방 번호 
    sum_dist = 0 #이동거리합
    for j in range(n):
        dist = (j - i + n) % n
        sum_dist += dist * people[j]

    min_val = min(min_val, sum_dist)


print(min_val)