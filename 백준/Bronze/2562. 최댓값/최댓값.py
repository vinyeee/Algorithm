nums = []

for _ in range(9):
    n = int(input())
    nums.append(n)

max_nums = max(nums) # 최댓값
print(max_nums)
print(nums.index(max_nums) + 1) #몇 번째 수인지 출력 인덱스 + 1