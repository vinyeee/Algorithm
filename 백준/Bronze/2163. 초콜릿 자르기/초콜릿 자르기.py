import sys
n,m = map(int,sys.stdin.readline().split())

# N X M 초콜릿을 1 X M 초콜릿 N개로 나누기 위해서 N - 1번 잘라야함 
# 1 X M개의 초콜릿을 1 X 1 초콜릿 M 개로 자르려면 M - 1 번 잘라야함 

cutting_count = (n - 1) + n * (m - 1) 

print(cutting_count)