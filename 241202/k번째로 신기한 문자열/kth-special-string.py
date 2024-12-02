import sys
input = sys.stdin.readline

n,k,t = input().split()

n = int(n)
k = int(k)

_list = []

for _ in range(n):
    word = input().strip()
    l = len(t)
    if t == word[:l]:
        _list.append(word)

_list.sort()

print(_list[k-1])




