n = int(input())
_list = list(map(int, input().split()))


## 그냥 반복문 
def lcm(a,b):
    min_val = min(a,b)
    lcm = 0
    for i in range(1,min_val + 1):
        if a % i == 0 and b % i == 0:
            lcm = i
    return lcm 
## 유클리드 호재 법
# def lcm(a,b):


## 최소 공배수 성질 : 두 수의 곱을 최대 공약수로 나누면 최소 공배수가 됨  
def gcd(a,b):
    return a * b // lcm(a,b)


gcd_num = gcd(_list[0], _list[1])
for i in range(2,n):
    gcd_num = gcd(gcd_num, _list[i])
print(gcd_num)