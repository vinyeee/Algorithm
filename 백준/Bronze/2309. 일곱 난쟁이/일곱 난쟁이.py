from itertools import combinations


heights = [int(input()) for _ in range(9)]


for i in combinations(heights,7):
    heights_sum = sum(i)
    if heights_sum == 100:
        for j in sorted(i):
            print(j)
        
        break