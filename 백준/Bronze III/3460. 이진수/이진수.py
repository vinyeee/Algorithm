import sys
t = int(sys.stdin.readline()) #테스트 케이스 갯수

for i in range(t):
    n = int(sys.stdin.readline())
    #print(bin(n))
    binary_n = bin(n)
    for i in range(len(binary_n)-1 , 1, -1):
        if binary_n[i] == '1':
            print(len(binary_n)-1 - i,end=' ')