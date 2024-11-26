y = int(input())

def is_yun_year(y):
    if y % 4 != 0 :
        return False
    if y % 100 == 0 and y % 400 != 0 :
        return False 

    return True



print("true" if is_yun_year(y) else "false")

