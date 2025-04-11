def solution(price, money, count):
    answer = -1
    
    total = sum([i * price for i in range(1,count+1)])
    answer = total - money 
    return answer if answer > 0 else 0    
    