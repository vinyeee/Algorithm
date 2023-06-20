import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(r,depth):
	#01
    visited[r]=depth
    graph[r].sort()
    for i in graph[r]:
    	#02
        if visited[i]==-1:
            dfs(i,depth+1)
#03
dfs(r,0)
for i in visited[1:]:
    print(i)
