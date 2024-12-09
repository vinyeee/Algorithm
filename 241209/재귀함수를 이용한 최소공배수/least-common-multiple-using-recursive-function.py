n = int(input())
_list = list(map(int, input().split()))


## 그냥 반복문 
# def lcm(a,b):
#     min_val = min(a,b)
#     lcm = 0
#     for i in range(1,min_val + 1):
#         if a % i == 0 and b % i == 0:
#             lcm = i
#     return lcm 
## 유클리드 호재법 : a,b 의 최대 공약수는 b와 a%b 의 최대 공약수와 같음 (a > b)
def lcm(a,b):
    if a < b :
        a,b = b,a
    if b == 0: #나누어 떨어지면 작은수가 최대 공약수
        return a
    return lcm(b,a%b)



## 최소 공배수 성질 : 두 수의 곱을 최대 공약수로 나누면 최소 공배수가 됨  
def gcd(a,b):
    return a * b // lcm(a,b)


gcd_num = gcd(_list[0], _list[1])
for i in range(2,n):
    gcd_num = gcd(gcd_num, _list[i])
print(gcd_num)