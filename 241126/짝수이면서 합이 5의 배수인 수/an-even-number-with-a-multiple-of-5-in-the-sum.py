n = input()

def is_even_and_5multiple(n):
    a = int(n[1]) #일의자리
    b = int(n[0]) #십의 자리
    return True if int(n) % 2 == 0 and (a+b) % 5 == 0 else False


if is_even_and_5multiple(n):
    print("Yes")
else:
    print("No")