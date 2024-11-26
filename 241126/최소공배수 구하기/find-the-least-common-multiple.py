n,m = map(int,input().split())



def find_gcd(n,m):
    gcd = 1
    for i in range(2, min(n,m)):
        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd
    
def find_lcm(n,m):
    #둘의 공약수 중 가장 큰 수를 x라 하면  
    x = find_gcd(n,m)
    a = n // x
    b = m // x
    lcm = x * a * b 
    return lcm




print(find_lcm(n,m))