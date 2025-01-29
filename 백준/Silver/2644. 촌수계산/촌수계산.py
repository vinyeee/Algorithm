import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
n = int(input().strip())  # 사람 수
p1, p2 = map(int, input().strip().split())  # 촌수 계산할 두 사람
m = int(input().strip())  # 관계 개수

# 그래프(인접 리스트) 만들기
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향(부모-자식 관계)

# 방문 체크 배열 (함수 밖으로 이동)
visited = [False] * (n + 1)

# BFS 함수
def bfs(start, target):
    queue = deque([(start, 0)])  # (현재 노드, 촌수)
    visited[start] = True  # 시작 노드 방문 처리
    
    while queue:
        now, count = queue.popleft()
        
        if now == target:
            return count  # 촌수 반환
        
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, count + 1))  # 촌수 증가
    
    return -1  # 관계 없음

# 결과 출력
print(bfs(p1, p2))
