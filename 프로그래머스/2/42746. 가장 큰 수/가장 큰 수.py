
from functools import cmp_to_key

def solution(numbers):
    
    str_nums = list(map(str,numbers))
    
    answer = ''

    def cmp_str(x,y):
        if x + y > y + x :
            return -1
        elif x + y < y + x:
            return 1
        else :
            return 0
    
    sorted_str_nums = sorted(str_nums, key =cmp_to_key(cmp_str))
    
    answer = answer.join(sorted_str_nums)
    return '0' if int(answer) == 0 else answer