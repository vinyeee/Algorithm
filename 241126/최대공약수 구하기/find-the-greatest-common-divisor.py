n,m = map(int, input().split())

#완전 탐색으로 풀기 
def find_gcd(n,m):

    gcd = 1
    for i in range(2, min(n,m)+1):
        if n % i == 0 and m % i == 0 :
            gcd = i 
    return gcd


print(find_gcd(n,m))
