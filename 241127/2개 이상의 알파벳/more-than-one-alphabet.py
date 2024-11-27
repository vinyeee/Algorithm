a = input()
 


def have_another_alphabets(string):
    
    alphabets = []
    for s in string:
        if s not in alphabets:
            alphabets.append(s)
    if len(alphabets) >= 2:
        return True
    return False 




if have_another_alphabets(a):
    print("Yes")
else:
    print("No")