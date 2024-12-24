x,y = map(int, input().split())


max_val = 0
for i in range(x, y+1):
    digit_sum = sum(list(map(int,list(str(i)))))

    max_val = max(max_val, digit_sum)

print(max_val)