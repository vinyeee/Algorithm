def fibo(n):

    fibo = [0,1]

    if n == 0:
        return fibo[0]
    elif n == 1:
        return fibo[1]
    else:
        for i in range(2,n+1):
            fibo.append(fibo[i-1] + fibo[i-2])

    
    return fibo[n]

n = int(input())


print(fibo(n))

