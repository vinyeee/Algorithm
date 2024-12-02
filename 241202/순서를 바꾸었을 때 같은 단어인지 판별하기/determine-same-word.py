a = list(input())
b = list(input())

a.sort()
b.sort()



def is_same_elements():
    if len(a) != len(b):
        return False
    
    for elem1 , elem2 in zip(a,b):
        if elem1 != elem2:
            return False
    return True



if is_same_elements():
    print("Yes")
else:
    print("No")
