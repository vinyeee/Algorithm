a,b = map(int, input().split())

def power(a,b):

    result = 1
    for _ in range(b):
        result *= a
    return result
    
print(power(a,b))