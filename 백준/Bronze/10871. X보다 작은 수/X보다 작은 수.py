
n, x = map(int, input().split())
nums = list(map(int,input().split()))

#print(nums)

for i in range(n):
    if (nums[i] < x):
        print(nums[i], end = ' ')
