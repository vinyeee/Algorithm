import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input().strip())
cards = list(map(int, input().strip().split()))
cards.sort()
m = int(input().strip())
arr = list(map(int, input().strip().split()))


def bi_count(a):
    start = bisect_left(cards,a)
    end = bisect_right(cards, a)
    return end - start

answer = []
for a in arr:
    cnt = bi_count(a)
    answer.append(cnt)

print(" ".join(list(map(str,answer))))