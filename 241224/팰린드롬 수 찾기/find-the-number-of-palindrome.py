x,y = map(int, input().split())


def is_pallindrom(s):
    if s == s[::-1] :
        return True
    return False


cnt = 0
for i in range(x, y + 1):
    if is_pallindrom(str(i)):
        cnt += 1


print(cnt)