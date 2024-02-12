import sys
n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
b,c = map(int, sys.stdin.readline().split()) #총감독, 부감독이 맡을 수 있는 인원수

count = 0 
A = list(map(lambda x: x - b, A))
count += n 
#print(A)

for i in range(n):
    ai = A[i]    
    if ai > 0 :
        if ai % c == 0:
            count += ai // c
        else:
            count += ai // c + 1
            


print(count)
        

