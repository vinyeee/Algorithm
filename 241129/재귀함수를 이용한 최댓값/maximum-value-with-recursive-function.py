n = int(input())
arr = list(map(int,input().split()))

max_val = arr[n - 1]

def find_max(n):
    global max_val
    if n  < 0:
        return 
    if max_val < arr[n]:
        max_val = arr[n]    
    return find_max(n - 1)

find_max(n - 2)
print(max_val)