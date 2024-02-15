'''
n의 k번 째로 작은 약수를 구해라
'''
import sys
n,k = map(int, sys.stdin.readline().split())

count = 0

for i in range(1,n+1):
    if n % i == 0:
        count += 1
        if count == k:
            print(i)

if count < k:
    print(0)