n = int(input())




def print_starts(n):
    if n == 0 :
        return 
    print("* " * n)
    print_starts(n - 1)
    print("* " * n)

print_starts(n)