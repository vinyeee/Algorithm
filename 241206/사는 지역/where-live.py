n = int(input())

people = []
for i in range(n):
    people.append(tuple(input().split()))

name = people[0][0]

idx = 0
for i in range(1,n):
    if name < people[i][0]:
        idx = i


print(f"name {people[idx][0]}\naddr {people[idx][1]}\ncity {people[idx][2]}")



