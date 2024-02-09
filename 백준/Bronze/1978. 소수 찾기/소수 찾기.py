'''
소수 찾기


'''

count= 0


def identify_prime(factor):
    
    if factor < 2 :
        # 1은 소수가 아님 
        return False
    else:
        for div in range(2, factor):
            if factor % div == 0:
                return False
            
        return True
    
            
    

def main():

    global count
    n = int(input())

    numbers = list(map(int, input().strip().split()))

    for factor in numbers:
        if identify_prime(factor):
            count += 1
    
    print(count)


main()