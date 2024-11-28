n = int(input())

def one_to_n_sum(n):
    if n == 1:
        return 1
    return one_to_n_sum(n - 1) + n 


print(one_to_n_sum(n))