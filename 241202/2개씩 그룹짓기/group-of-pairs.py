n = int(input())
arr = list(map(int, input().split()))

arr.sort()


# [5, 5, 3, 2]
_list =[]
for i in range(n):
    _list.append(arr[i] + arr[2*n-i-1])
    
print(max(_list))

