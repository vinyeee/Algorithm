
import sys
input = sys.stdin.readline

n = int(input().strip())
cards = list(map(int,input().strip().split()))
cards.sort(reverse= True)


gold = 0
level = cards[0]

for i in range(1,n):
    x = level + cards[i]
    gold += x


print(gold)
