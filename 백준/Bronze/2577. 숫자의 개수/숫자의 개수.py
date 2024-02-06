A = int(input())
B = int(input())
C = int(input())

n_string = str(A * B * C)

count_lst = [0] * 10

for n in n_string:
    index = int(n)
    count_lst[index] += 1


for i in range(10):
    print(count_lst[i])