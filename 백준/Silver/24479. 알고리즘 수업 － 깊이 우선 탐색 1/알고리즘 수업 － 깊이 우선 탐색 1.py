import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)]
chk = [0] * (N+1)
cnt = 0

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(now):
    global cnt 
    cnt += 1
    chk[now] = cnt #맨처음 방문한 노드는 1, 두번째 방문노드는 2 ... 방문하지 않은 노드에는 0 이 저장되게 된다
    for i in graph[now]:
        if not chk[i]:
            dfs(i)




#오름차순으로 방문하기 위해 그래프의 인접리스트들을 정렬해줌
for i in range(1,N+1):
    graph[i].sort()

dfs(R) # 그 다음에 dfs호출

for i in range(1,N+1):
    print(chk[i])