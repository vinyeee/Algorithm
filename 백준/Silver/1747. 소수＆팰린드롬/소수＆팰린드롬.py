
'''
소수이면서 팰린드롬 인 수 
1. 소수조건 : for 문 돌면서 나누어 떨어지지 않음 
2. 팰린드롬 : 
'''
import sys
from collections import deque
import math

n = int(sys.stdin.readline())
#strn = deque(str(n))
#print(strn)
def isPalindrome(n):
    dq = deque(str(n))
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return 0
    return 1

def isPrime(n):
   
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    if isPrime(n) and isPalindrome(n):
        print(n)
        break
    else:
        n += 1