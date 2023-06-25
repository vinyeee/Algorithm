
result = []

for i in range(10):
    n = int(input())
    if n % 42 not in result:
        result.append(n % 42)


print(len(result))