'''
1. 알고리즘
- 백트래킹에다가 오름차순 판단 집어넣기
2. 시간복잡도
- 중복이 없으니까 n은 최대 10까지 가능 
3. 자료구조
- 방문체크 boolean배열 
- 결과를 저장할 int 배열 
'''

import sys

input = sys.stdin.readline
n,m = map(int, input().split())

result = []
visited = [False] * (n + 1)
def recur(start):
    if start == m + 1:
        print(' '.join(map(str, result)))
        return 
    
    for i in range(start, n+1): #방문 하지 않았고 리스트 맨 마지막에 있는 것보다 크면 담음 
        if not visited[i] and (len(result) == 0 or result[-1] < i ) :
            
            visited[i] = True
            result.append(i)
            recur(start + 1)
            visited[i] = False
            result.pop()


recur(1)

