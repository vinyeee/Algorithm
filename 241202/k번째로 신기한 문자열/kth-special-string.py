n,k,t = input().split()

n = int(n)
k = int(k)

_list = []

for word in range(n):
    if t in word:
        _list.append(word)

_list.sort()

print(_list[k-1])




