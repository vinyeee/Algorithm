'''
1. 알고리즘
    이진 탐색 라이브러리 사용 
    1) 상근이가 가지고 있는 카드 배열을 sort  
    2) 주어진 m개의 숫자가 들어있는 배열 arr에서 for문으로 원소 하나씩 꺼냄 
    3) 각 원소마다 cards 배열에서 이진탐색 진행 
    4) 이진 탐색의 결과에 따라 1,0d을 answer 배열에 append
    
2. 시간복잡도
    1 <= n , m <= 500000 이고 완전탐색으로 푼다면 m개에 대해서 n개의 원소가 들어있는
    배열을 탐색해야하기 때문에 25 *  10 ^ 10  < 4억 (4 * 10 ^ 8) => 시간초과
    따라서 완전 탐색이 아닌 이진탐색으로 접근 
    시간 복잡도는 => 5 * 10^5 log 5*10^5 < 4억
3. 자료구조
    이진 탐색 결과를 집어넣을 answer[]

    -밀라 님께 이진탐색 파이썬 코드를 직접 구현할 수 있게 외우는게 좋을지
    아니면 bisect 라이브러리 쓰는게 나은지 여쭤보기  
'''

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().strip()) 
cards = list(map(int, input().strip().split()))
cards.sort()

m = int(input().strip())
arr = list(map(int, input().strip().split()))


answer = []

for i in range(m):
    idx = bisect_left(cards,arr[i]) #이진 탐색으로 찾은 인텍스 
    #인덱스 값이 n-1 보다 크면 확실히 배열에 존재하지 않음 
    if idx > n - 1 :
        answer.append(0)
    else: #인텍스 값이 0<= idx <= n-1 이면 실제 그 인덱스 값과 비교해서 판단 
        if arr[i] == cards[idx]:
            answer.append(1)
        else:
            answer.append(0)

print(" ".join(list(map(str, answer))))

