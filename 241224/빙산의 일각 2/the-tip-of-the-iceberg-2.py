n = int(input())
arr = [int(input()) for _ in range(n)]

max_num = 0
for i in range( max(arr)):
    copy_arr = arr[:]
    for j in range(n):
        copy_arr[j] -= i
    num =len(''.join(list(map(str,copy_arr))).split('0'))
    max_num = max(max_num, num)
print(max_num)




    
    
