a,b = map(int, input().split())


def new_number(a,b):
    if a > b:
        return a+25 , b*2
    else:
        return a*2 , b+25 

a,b = new_number(a,b)
print("{} {}".format(a,b))