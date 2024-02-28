import heapq
import sys

n = int(sys.stdin.readline())

max_heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(max_heap,(-x,x))
    #print(max_heap)
