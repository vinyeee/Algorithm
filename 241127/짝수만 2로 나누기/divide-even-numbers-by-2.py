n = int(input())
arr = list(map(int,input().split()))

def divide_2(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
    


divide_2(arr)

for a in arr:
    print(a, end = " ")