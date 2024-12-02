n,k,t = input().split()

n = int(n)
k = int(k)

_list = []

for _ in range(n):
    word = input()
    if t == word[:2]:
        _list.append(word)

_list.sort()

print(_list[k-1])




