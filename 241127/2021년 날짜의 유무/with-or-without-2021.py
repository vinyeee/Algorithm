m,d = map(int, input().split())




def last_day_number(m):
    #2월은 28
    if m == 2:
        return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31 




def judge_day(m,d):
    if m <= 12 and d <= last_day_number(m): #1~12월 이고 해당월의 마지막 날짜 범위 내에 있으면 
        return True
    return False



if judge_day(m,d):
    print("Yes")
else:
    print("No")