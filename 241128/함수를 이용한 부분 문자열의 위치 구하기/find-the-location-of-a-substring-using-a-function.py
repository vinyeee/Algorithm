string = input()
part_string = input()

n = len(string)
m = len(part_string)
idx = 0

def is_start_index(i):
    for j in range(m):
        if string[j + i] != part_string[j]: #i는 부분문자열이 시작될 가능성이 입력 문자열의 있는 인덱스 , j는 부분문자열 인덱스 
            return False
    return True


def is_part_string():
    global idx
    for i in range(n - m + 1):
        #부분 문자열 시작 인덱스
        if is_start_index(i):
            idx = i
            return True
    return False


if is_part_string():
    print(idx)
else:
    print(-1)
