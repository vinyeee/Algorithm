


def is_palindrome(str_num):

    buffer = []
    for i in range(len(str_num) -1 , -1, -1):
        buffer.append(str_num[i])
    #print(buffer)

    result = "".join(buffer)

    #print(result)
    if (result == str_num):
        print("yes")
    else:
        print("no")
    

while True:
    str_num = input().strip()
    if str_num == '0':
        break
    else:
        is_palindrome(str_num)