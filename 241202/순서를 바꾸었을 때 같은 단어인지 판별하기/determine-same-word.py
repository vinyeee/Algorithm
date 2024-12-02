a = input()
b = input()

a = list(a)
b = list(b)

a.sort()
b.sort()

def is_same_element():
    for elem1, elem2 in zip(a,b):
        if elem1 != elem2:
            return False
    return True


if is_same_element():
    print("Yes")
else:
    print("No")