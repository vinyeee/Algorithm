import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u) #무방향, 양방향 리스트 


'''
[]
[4, 2]
[1, 3, 4]
[2, 4]
[1, 2, 3]
[]
'''
chk = [0 for _ in range(N+1)]
cnt = 0 

def dfs(now):
    global cnt 
    cnt += 1
    chk[now] = cnt

    for nxt in graph[now]:
        if not chk[nxt]:
            dfs(nxt)



#graph 내림차순으로 정렬
for i in range(1,N+1):
    graph[i].sort(reverse=True)
   

dfs(R)

for i in range(1,N+1):
    print(chk[i]) 