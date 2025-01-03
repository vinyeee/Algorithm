'''1. 알고리즘 
총 n개의 집들 중 k개의 대피소를 정해야 하기에 일반적인 for문으로 돌리면 k번 for문을 돌아야하기 때문에 
combinations을 써서 n개의 집들 중 k개의 대피소를 정해두고 각 대피소에서 가장 가까운 거리를 
구해주고 그 거리들 중에 가장 큰 값을 찾는다 

k개의 대피소가 바뀔 때마다 가장 큰 값을 갱신해준다 << 완전탐색

'''
from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
houses = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 최소값을 매우 큰 값으로 초기화
min_max_min_dist = sys.maxsize

# n개의 집들 중에서 k개의 대피소를 선택하는 모든 조합을 순회
for shelters in combinations(range(n), k):
    # 현재 대피소 조합에서 가장 큰 최소 거리를 찾기 위한 변수
    max_min_dist = 0
    
    # 각 집에 대해서
    for cur_house in range(n):
        house = houses[cur_house]
        
        # 해당 집에서 가장 가까운 대피소까지의 거리 계산
        min_dist = sys.maxsize
        for shelter_idx in shelters:
            shelter = houses[shelter_idx]  # 대피소의 좌표는 houses에서 가져오기
            d = abs(house[0] - shelter[0]) + abs(house[1] - shelter[1])
            min_dist = min(min_dist, d)
        
        # 해당 집에서 가장 가까운 대피소까지의 거리 중 최대값을 계산
        max_min_dist = max(max_min_dist, min_dist)

    # 여러 대피소 조합 중 가장 작은 최대 거리를 찾기
    min_max_min_dist = min(min_max_min_dist, max_min_dist)

# 결과 출력
print(min_max_min_dist)