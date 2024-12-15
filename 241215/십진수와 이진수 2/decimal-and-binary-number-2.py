binary = list(map(int, input()))
n = len(binary)

decimal = 0

for i in range(n):
    decimal += binary[i] * (2 ** (n - 1 - i))



decimal *= 17

def deciaml_to_binary(decimal):

    digits = []
    
    while True:

        if decimal < 2:
            digits.append(decimal)
            break

        digits.append(decimal % 2)
        decimal //= 2

    for digit in digits[::-1]:
        print(digit, end = "")




deciaml_to_binary(decimal)
