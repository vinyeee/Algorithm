a,b = map(int, input().split())


def have_3_6_9(i):
    string_i = str(i)
    for s in string_i:
        if s == "3" or s == "6" or s=="9":
            return True
    return False


def is_magic_number(i):
    return i % 3 == 0 or have_3_6_9(i)


cnt = 0
for i in range(a,b+1):
    if is_magic_number(i):
        cnt += 1

print(cnt)