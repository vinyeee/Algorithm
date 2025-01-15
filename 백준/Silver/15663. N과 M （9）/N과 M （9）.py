import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
#중복제거 -> 리스트 -> sort
n_list = list(map(int, input().strip().split()))
n_list.sort()


visited = [False] * n 
'''
1이라는 원소 방문 -> visited[1] = True 가 아니라 
1번째 원소 방문 -> visited[1] = True

이렇게 하면 n_list 가 1 1 1 1 로 중복되는 수로 이루어져 있어도 원소별로 방문했는지 안했는지 구분 가능
같은 1이라도 각 자리에 있는 1은 모두 다른 1 
'''
result = []

def recursion(cnt):

    if cnt == m :
        print(" ".join(map(str, result)))
        return
    
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != n_list[i]: 
            visited[i] = True
            result.append(n_list[i])
            overlap = n_list[i]
            recursion(cnt + 1)

            visited[i] = False
            result.pop()

recursion(0)
