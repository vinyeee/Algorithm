n = int(input())

string = input()

cnt = 0 

for i in range(n):
    if string[i] == 'C':
        for j in range(i + 1, n) :
            if string[j] == 'O':
                for k in range(j + 1, n):
                    if string[k] == 'W':
                        cnt += 1


print(cnt)
                        
                