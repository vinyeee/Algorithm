n, k = map(int, input().split())

k= k + 1
people = [0] * (10000 + 1)

for _ in range(n):
    idx , alphabet = input().split()
    if alphabet == 'G':
        people[int(idx)] = 1
    else:
        people[int(idx)] = 2


max_score = 0
for i in range(1,10000 - k + 2):
    score = 0
    for j in range(i, i + k):
        score += people[j]
    max_score = max(max_score, score)

print(max_score)