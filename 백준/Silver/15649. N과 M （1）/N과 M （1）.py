'''
1. 아이디어
    - 백트래킹 재귀함수 안에서, for 문을 돌면서 숫자 선택 (이때 방문여부 체크)
    - 재귀함수에서 M만큼 깊어지면 print

2. 시간복잡도
    - 중복이 가능하면N ^ N (N = 8 까지 가능)
    - 중복이 불가능하면 N! (N = 10 까지 가능)
3. 자료구조
    - 결과 값을 저장할 int 배열
    - 방문 여부 체크하는 boolean 값 

    백트래킹은 n이 작다
    재귀 함수 사용할 떄, 종료 조건 부터 먼저 적고 시작 
'''


import sys
input = sys.stdin.readline

n , m = map(int, input().split())
result = []
visited = [False] * (n + 1)


def recur(num):
    if num == m:
        print(' '.join(map(str, result))) #??
        return 
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            recur(num + 1) #리턴되서 돌아온 다음 
            
            visited[i] = False #다시 방문 안했다고 바꿔주고고
            result.pop()#맨 뒤에 값을 빼줌 
recur(0)