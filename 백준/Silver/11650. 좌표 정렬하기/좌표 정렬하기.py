import sys

n = int(sys.stdin.readline())

points = []

for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    points.append([x,y])


points.sort()
#print(points)


for p in points:
     print(f"{p[0]} {p[1]}")