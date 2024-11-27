_str = input()


def string_reverse(_str):
    new_str = ""
    for i in range(len(_str)-1,-1,-1):
        new_str += _str[i]
    return new_str
    


new_str = string_reverse(_str)


if (_str == new_str):
    print("Yes")
else:
    print("No")