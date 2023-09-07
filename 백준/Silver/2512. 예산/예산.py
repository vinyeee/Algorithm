N = int(input()) # 지방의 개수
req = list(map(int, input().split())) # 각 지방의 요청 예산액
M = int(input()) # 정부 예산 총액


lo = 0
hi = max(req)
mid = (lo + hi) // 2
ans = 0


def is_possible(mid):
    return sum(min(r,mid) for r in req) <= M
    

while lo <= hi:
    #print(f"lo:{lo} mid:{mid} hi:{hi} ans:{ans}")
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1
    
    mid = (lo + hi) // 2

print(ans)