a,b = map(int, input().split())


def change_number(a,b):
    if a > b :
        return a * 2 , b + 10
    else:
        return a + 10 , b * 2

a,b = change_number(a,b)

print(f"{a} {b}")