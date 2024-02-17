import sys

a,b = map(int, sys.stdin.readline().split())

def make_sequence():
    s = [0] * 1001
    start = 1 # 인덱스 위치를 알려줄 변수  
    num = 1 #인덱스에 채울 숫자 
    cnt = 0


    while cnt <= 1000:
        if start + num <= 1000:
            for i in range(start, start + num):
                #print(cnt)
                s[i] = num
                cnt += 1
            start += num
            num += 1
        else:
            for i in range(start, 1001):
                s[i] = num
                cnt += 1

    return s


def section_sum(a,b,s):
    sum = 0
    for i in range(a,b+1):
        sum += s[i]

    return sum

s = make_sequence()
#print(s)
print(section_sum(a,b,s))