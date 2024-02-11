import sys

while True:
    a,b,c = map(int, sys.stdin.readline().strip().split())
    if (a == 0 and b == 0 and c == 0):
        break

    lines = [a,b,c]
    max_val = max(lines)
    lines.remove(max_val)
    if (max_val**2 == lines[0]**2 + lines[1]**2):
        print("right")
    else:
        print("wrong")