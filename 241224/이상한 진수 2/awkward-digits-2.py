a = input()
n = len(a)

def binary_to_decimal(new_a):
    decimal = 0
    n = len(new_a)
    for i in range(n):
        decimal += int(new_a[i]) * (2 ** (n - i - 1))
    return decimal


max_val = 0
for i in range(n):
    original = a[i]

    filpped_bit = '0' if a[i] == '1' else '1'

    modified_a = a[:i] + filpped_bit + a[i + 1:]

    decimal_a = binary_to_decimal(modified_a)

    max_val = max(max_val, decimal_a)


print(max_val)


    
    

    


