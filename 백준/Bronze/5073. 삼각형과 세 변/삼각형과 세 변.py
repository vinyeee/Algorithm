import sys

while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if (a == 0 and b == 0 and c == 0):
        break
    max_line = max(a,b,c)
    if (max_line >= sum([a,b,c]) - max_line):
        print("Invalid")
    elif (a == b == c):
        print("Equilateral") #세 변의 길이가 같은 경우
    elif(a == b or b == c or a == c):
        print("Isosceles")
    else:
        print("Scalene")
          