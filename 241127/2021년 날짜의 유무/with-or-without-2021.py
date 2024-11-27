m,d = map(int, input().split())


def is_valid_day(m,d):
    if m == 2 and ( d < 1 or d > 28):
        return False
    if m == 8 and ( d < 1 or d > 31):
        return False
    if m % 2 == 0 and ( d < 1 or d > 30):
        return False
    if m % 2 != 0 and ( d < 1 or d > 31):
        return False
    return True



def is_valid_month(m,d):

    if m < 1 or m > 12:
        return False
    if not is_valid_day(m,d):
        return False
    return True

if is_valid_month(m,d):
    print("Yes")
else:
    print("No")