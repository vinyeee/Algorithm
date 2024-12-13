import sys
developer = list(map(int, input().split()))

MAX_INT = sys.maxsize

min_val = MAX_INT

def get_diff(i,j,k):
    team1 = developer[i] + developer[j] + developer[k]
    team2 = sum(developer) - team1
    return abs(team1 - team2)

n = 6

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            min_val = min(min_val, get_diff(i,j,k))


print(min_val)
