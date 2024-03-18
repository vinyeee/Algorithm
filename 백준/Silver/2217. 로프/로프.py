import sys
n  = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]

#print(rope)
rope.sort(reverse= True) #중량이 큰 로프 순으로 정렬
#print(rope)

max = 0
for i in range(len(rope)):
    if rope[i] * (i+1) > max:
        max = rope[i] * (i+1)

print(max)