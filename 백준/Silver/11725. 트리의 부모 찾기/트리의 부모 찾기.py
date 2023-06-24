import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input()) #노드의 개수

tree = [ [] for _ in range(n + 1)]
chk = [0] * (n + 1) #방문 체크 

for i in range(n - 1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

'''
[]
[6, 4]
[4]
[6, 5]
[1, 2, 7]
[3]
[1, 3]
[4]

각 노드의 부모 노드를 출력 하자
'''

def dfs(now):
    for nxt in tree[now]:
        if not chk[nxt]:
            chk[nxt] = now
            dfs(nxt) 

dfs(1)

for i in range(2,n+1):
    print(chk[i])

