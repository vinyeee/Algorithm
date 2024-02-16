import sys
n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
#print(nums)
max_value = max(nums)   
min_value = min(nums)

print(f"{min_value} {max_value}")