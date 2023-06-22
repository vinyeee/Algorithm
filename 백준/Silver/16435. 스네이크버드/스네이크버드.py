n,l = map(int,input().split()) # 과일의 개수, 스네이크 버드의 초기 길이 
fruits = input().split()

fruits = [int(_) for _ in fruits]
fruits.sort()
fruits_copy = fruits.copy()


def greedy():
    global l 
    for fruit in fruits_copy:
        if (l >= fruit): #뱀새의 길이가 과일 높이보다 크거나 같으면
            fruits.remove(fruit)
            l += 1
    return l


print(greedy())