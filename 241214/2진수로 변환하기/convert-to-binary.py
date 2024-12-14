n = int(input())

digits = []
while True:

    if n < 2:
        digits.append(str(n))
        break
        
    digits.append(str(n % 2))
    n //= 2



print("".join(digits[::-1]))