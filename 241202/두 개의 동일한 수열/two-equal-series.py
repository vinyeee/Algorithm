
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_same_element():
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True    




if is_same_element():
    print("Yes")
else:
    print("No")