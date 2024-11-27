y,m,d = map(int, input().split())




def judge_season(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    else:
        return "Winter" 

def is_yun_year(y):
    # if y % 4 != 0 :
    #     return False
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 == 0:
        return False
    return False
    

def last_day_number(y,m):
    if is_yun_year(y):
        if m == 2:
            return 28
        else:
            return 29
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30 
    else:
        return 31  



def judge_day(y,m,d): #해당 날짜가 존재하는지 확인 
    if 1 <= m <= 12 and 1 <= d <= last_day_number(y,m):
        return True
    return False


if judge_day(y,m,d):
    result = judge_season(m)
else:
    result = -1

print(result)