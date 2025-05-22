K, N = map(int, input().split())

# Please write your code here.

answer = []

def print_answer():
    print(*answer)



def recur(num):
    if num == N + 1:
        print_answer()
        return 
    
    for i in range(1, K+1):
        answer.append(i)
        recur(num+1)
        answer.pop()
    
    return 


recur(1)