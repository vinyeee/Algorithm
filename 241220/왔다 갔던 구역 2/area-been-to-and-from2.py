n = int(input())

MAX_R = 2000 # 10칸씩 100번 움직이면 
OFFSET = 1000
checked = [0] * (MAX_R + 1)

start = 1000

for i in range(n):
    x , cmd = input().split()
    x = int(x)
    if cmd == 'R':
        for j in range(start , start + x):
            checked[j] += 1
        start += x 
    else:
        for j in range(start - 1 , start - 1 - x , -1):
            checked[j] += 1
        start -= x
        
                
cnt = 0
for i in range(len(checked)):
    if checked[i] >= 2:
        cnt += 1
print(cnt)
