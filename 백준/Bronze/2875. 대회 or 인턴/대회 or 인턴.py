'''
여 , 남 , 인턴쉽에 참여해야하는 인원 수 

k 명을 인턴쉽 보내고도 3명이상 남아있고
여자 2 명이상
남자 1 명이상 일때까지 팀을 짤 수 있다.

'''

import sys
input = sys.stdin.readline


n, m , k = map(int, input().strip().split())

t = 0 
while n >= 2 and m >= 1 and n + m - k >= 3 :
   
    n -= 2
    m -= 1
    t += 1


print(t)