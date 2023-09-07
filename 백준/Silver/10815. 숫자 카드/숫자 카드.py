from bisect import bisect_left

N = int(input()) # 10^5
cards = list(map(int,input().split()))
cards.sort()

M = int(input())
trial = list(map(int,input().split()))

#print(f"N:{N} 상근:{cards} M:{M} trial:{trial}")

ans = []
for t in trial:
    l = bisect_left(cards, t) #cards 에서 t이상인 값 중 첫번째 인덱스 
    if l <= len(cards) - 1 :
        if cards[l] == t:
            ans.append(1)
        else:
            ans.append(0)
    else:
        ans.append(0)

for _ in ans:
    print(_, end=" ")