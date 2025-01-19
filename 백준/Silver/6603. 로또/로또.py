import sys
input = sys.stdin.readline



def combination(cnt, start):

    if cnt == 6:
        print(" ".join(map(str,result)))
        return
    
    for i in range(start,k):
        result.append(s[i])
        combination(cnt + 1, i + 1)
        result.pop()



while True:
    k_s = list(map(int, input().strip().split()))
    k, s = k_s[0], k_s[1:]
    result = []
    if k == 0:
        break

    combination(0, 0)

    print()