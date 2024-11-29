n = int(input())
arr = list(map(int, input().split()))

arr.sort()

print(" ".join(map(str,arr)))

arr = arr[::-1]

print(" ".join(map(str,arr)))

