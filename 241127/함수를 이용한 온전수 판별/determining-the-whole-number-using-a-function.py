a,b = map(int, input().split())



def is_magic_number(i):

    if i % 2 == 0:
        return False
    if i % 10 == 5: #일의 자리는 10으로 나눴을 때 나머지 
        return False
    if i % 3 == 0 and i % 9 != 0:
        return False
    return True



cnt = 0 

for i in range(a, b+1):
    if is_magic_number(i):
        cnt += 1


print(cnt)