from collections import deque




def is_balanced(line):

    stack = deque()
    
    for ch in line:
        
        if (ch == '(' or ch == '['):
            stack.append(ch)
        
        elif ch == ']': #닫는 괄호면
            if len(stack) == 0:
                return False
            value = stack.pop()
            if value != '[':
                return False
            
        elif ch == ')':
            if len(stack) == 0:
                return False
            value = stack.pop()
            if value != '(':
                return False
            
    if len(stack) == 0:
        return True
    

while True:
    line = input().rstrip()
    if line == '.':
        break

    if is_balanced(line):
        print("yes")
    else:
        print("no")