row, col = map(int, input().split())

def print_rect(row, col):
    for _ in range(row):
        print("1"*col)


print_rect(row,col)