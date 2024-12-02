n = int(input())
arr = list(map(int, input().split()))

for i in range(1,n+1):
    if i % 2 != 0: #홀수 번째 
        _list = arr[:i]
        _list.sort()
        print(_list[len(_list) // 2], end =" ")

