n = int(input())

def print_helloworld(n):
    if n == 0:
        return 
    print_helloworld(n - 1)
    print("HelloWorld")


print_helloworld(n)