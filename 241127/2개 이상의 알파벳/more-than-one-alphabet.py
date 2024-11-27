a = input()
 


def have_another_alphabets(string):

    for s in string:
        if s != string[0]:
            return True
    return False 




if have_another_alphabets(a):
    print("Yes")
else:
    print("No")