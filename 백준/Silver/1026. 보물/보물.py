import sys
input = sys.stdin.readline

n = int(input()) #배열 원소의 개수 
A = list(map(int,input().split()))
B = list(map(int,input().split()))


A.sort() 
B.sort(reverse = True)

s = 0
for i in range(n):
    s += A[i] * B[i]

print(s)