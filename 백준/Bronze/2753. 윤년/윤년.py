year = int(input()) #년도

if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):#윤년은 4의 배수이면서 100의 배수가 아님 또는 400의 배수
    result = 1
else :
    result = 0

print(result)