n = int(input())
arr = list(map(int,input().split()))



def abs_list(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

abs_list(arr)

for elem in arr:
    print(elem, end = " ")