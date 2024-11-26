n = int(input())

def print_rect(n):
    
    num = 1
    for i in range(n):
        for j in range(n):
            print( num % 10 , end = " ")
            num += 1
            if num == 10:
                num = 1
        print()
    
    

print_rect(n)
