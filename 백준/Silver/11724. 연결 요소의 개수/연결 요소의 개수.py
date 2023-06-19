import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
#print(f"정점:{N}, 간선:{M}")  # 정점과 간선

adj = [[0] * N for _ in range(N)]

for _ in range(M):  # M줄 만큼 간선 정보 받아들이기
    a, b = map(lambda x: int(x)-1, input().split())  # 1 2 => 0 1이 이어져있다고 판단
    adj[a][b] = adj[b][a] = 1

chk = [False] * N  # 방문 체크 배열 생성
cnt = 0  # 연결 요소 개수


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:  # 연결된 노드이고 방문하지 않은 노드이면
            chk[nxt] = True
            dfs(nxt)  # 계속해서 탐색


for i in range(N):
    if not chk[i]:  # 방문을 안했으면 not False => True
        chk[i] = True
        cnt += 1
        dfs(i)

print(cnt)