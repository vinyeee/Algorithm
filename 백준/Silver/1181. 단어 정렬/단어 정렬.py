import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]

words = sorted(set(words), key= lambda x : (len(x), x))


for i in range(len(words)):
    print(words[i])         