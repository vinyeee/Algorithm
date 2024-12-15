a, b = map(int, input().split())
n = list(map(int, input()))

#a진수로 표현된 n을 10진수로 

#10진수로 표현된 n을 다시 b진수로 변환 


def decimal_to_b(decimal):

    digits = []

    while True:

        if decimal < b:
            digits.append(str(decimal))
            break

        digits.append(str(decimal % b))
        decimal //= b

    num = "".join(digits[::-1])
    return num



def a_to_decimal(n):

    num = 0
    for i in range(len(n)):
        num += n[i] * (a ** (len(n) - 1 - i))
    return num 


decimal = a_to_decimal(n)
num = decimal_to_b(decimal)
print(num)
