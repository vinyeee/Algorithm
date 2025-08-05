'''
import sys, math
input = sys.stdin.readline

m,n = map(int, input().strip().split())


prime = [True for _ in range(n+1)] #처음에는 모든 수가 소수인 것으로 초기화 
prime[0] = False
prime[1] = False


for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i]: # i가 소수라면
        #i를 제외한 i의 모든 배수를 지움(=소수가 아니라고 해줌)
        for j in range(i+i, n+1, i):
            prime[j] = False

for i in range(m,n+1):
    if prime[i]:
        print(i)

'''

import sys, math
input =sys.stdin.readline

m,n = map(int, input().strip().split())



def is_prime(num):
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            return False
    return True


for i in range(m, n+1):
    if i == 1:
        continue
    if is_prime(i):
        print(i)
