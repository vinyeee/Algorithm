n,m = map(int, input().split())
arr = list(map(int, input().split()))


def add_arr_a1_to_a2(a1,a2):
    sum = 0
    for i in range(a1-1, a2):
        sum += arr[i]
    return sum 

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(add_arr_a1_to_a2(a1, a2))

