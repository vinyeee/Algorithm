string = input()

alphabets = [-1] * 26

for c in string:
    index = ord(c) - 97
    #print(index)
    if (alphabets[index] == -1): #아직 한 번도 등장하지 않은 문자라면 
        alphabets[index] = string.index(c)

for c in alphabets:
    print(c, end = ' ')