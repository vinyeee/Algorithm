for _ in range(int(input())): #T줄 만큼 반복
    stack = [] 
    isVPS = True
    for ch in input():
        if (ch =='('):
            stack.append(ch)
        else:
            if len(stack) > 0:
                stack.pop()
            else: # 닫는 괄호가 더 많은 경우 
                isVPS = False
                break

    
    if stack: #여는 괄호가 더 많은 경우
        isVPS = False


    print('YES') if isVPS else print('NO')