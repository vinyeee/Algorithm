import sys

while True:
    lines = list(map(int, sys.stdin.readline().split()))
    a = lines[0]
    b = lines[1]
    c = lines[2]

    if (a == 0 and b == 0 and c == 0):
        break
    max_line = max(lines)
    lines.remove(max_line)

    if (max_line >= sum(lines)):
        print("Invalid")
    elif (max_line * 2 == sum(lines)):
        print("Equilateral") #세 변의 길이가 같은 경우
    elif(max_line == lines[0] or max_line == lines[1] or lines[0] == lines[1]):
        print("Isosceles")
    else:
        print("Scalene")