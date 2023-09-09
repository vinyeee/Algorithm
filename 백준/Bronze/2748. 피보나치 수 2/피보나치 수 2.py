### 탑 다운 방식 - 최댓값 90을 넣으면 시간초과가 남  
### 재귀함수로 구현하게 되면 f(n) 를 너무 많이 호출하게 되서 캐싱 과정이 필요함



# def f(n):
#     if n == 1:
#         return 1
#     elif n == 0 :
#         return 0
#     return f(n - 1) + f(n - 2)

cache = [-1] * 91 # 0~90 번째 

cache[0] = 0
cache[1] = 1


def f(n):
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)
    
    return cache[n]

    

print(f(int(input())))