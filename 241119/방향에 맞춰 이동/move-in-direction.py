n = int(input())

x = 0
y = 0 

for _ in range(n):
    d,l = input().split()
    l = int(l)
    if d == "N":
        x,y = x,y+l
    elif d == "E":
        x,y = x+l,y
    elif d == "S":
        x,y = x,y-l
    elif d == "W":
        x,y = x-l,y
print(x,y)


