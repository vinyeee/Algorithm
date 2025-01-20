import sys
input = sys.stdin.readline

t = int(input().strip())

q = 25
d = 10
n = 5 
p = 1



for _ in range(t):
    c = int(input().strip()) 

    print( c // q, end = ' ') 
    c %= q 

    print( c // d, end = " ")
    c %= d

    print(c // n, end = " ")
    c %= n 

    print(c // p)
    



