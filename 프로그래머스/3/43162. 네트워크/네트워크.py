'''
1. 알고리즘
    bfs
2. 시간복잡도
    - v : 200 * 200 = 400
    - e : 4 * 200 * 200 
    - v + e = 5 * 40000 = 200000 < 2억 => 가능 
3. 자료구조
    - queue
'''
from collections import deque



    
def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(i):
        q = deque([i])
        while q:
            current = q.popleft()
            for j in range(n):
                if computers[current][j] == 1 and not visited[j]:
                    visited[j] = True
                    q.append(j)


    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(i)
            answer += 1


    return answer