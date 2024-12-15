binary = input()

decimal = 0
n = len(binary)
for i in range(n):

    decimal += int(binary[i]) * ( 2 ** (n - 1 - i))


print(decimal)
