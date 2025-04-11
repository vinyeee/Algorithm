#n을 3진법 상으로 표현 -> 3진법 뒤집음 -> 다시 10진법으로 표현

def decimal_to_3(n):
    tmp = ''
    while n :
        tmp += str(n % 3)
        n = n // 3
    return tmp

def solution(n): 
    answer = decimal_to_3(n)
    return int(answer, 3)