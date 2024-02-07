n = int(input())



for _ in range(n):
    total = 0
    score = 0

    result = input().strip()

    for r in result :
        if (r == 'O'): # O 가 나오면
            score += 1 #score를 1씩 늘려감 
            total += score
        else: # X가 나오면
            if (score > 0):
                score = 0 # 다시 0으로 초기화

    print(total)