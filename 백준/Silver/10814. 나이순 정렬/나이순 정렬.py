import sys
input = sys.stdin.readline

n= int(input().strip())

arr = []
for i in range(n):
    age, name = input().strip().split()
    arr.append((int(age), name))
    

arr.sort(key= lambda x : (x[0]))


for i in range(n):
    print(f"{arr[i][0]} {arr[i][1]}" )