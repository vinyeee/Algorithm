#n을 3진법 상으로 표현 -> 3진법 뒤집음 -> 다시 10진법으로 표현
def convert_to_decimal(n): #문자
    result = 0
    for i in range(len(n)):
        result += int(n[-1 - i]) * (3**i)  
        
    return result

def decimal_to_3(n):
    result = []
    while n // 3 != 0:
        result.append(str(n % 3))
        n = n // 3
    result.append(str(n))
    return "".join(result)

def solution(n): 
    
    answer = 0
    answer = decimal_to_3(n)
    return convert_to_decimal(answer)