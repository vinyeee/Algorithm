n = int(input())
arr = list(map(int,input().split()))

def find_max(i):
    if i == 0:
        return arr[0]
        
    return max(find_max(i-1),arr[i])


print(find_max(n-1))