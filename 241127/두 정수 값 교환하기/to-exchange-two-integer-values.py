n,m = map(int,input().split())


def swap(a,b):
    a,b = b,a
    return a,b 

n,m = swap(n,m)
print(n,m)

