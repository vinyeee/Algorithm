n,k,t = input().split()

n = int(n)
k = int(k)

_list = []

for _ in range(n):
    word = input()
    if t in word:
        _list.append(word)

_list.sort()

print(_list[k-1])




