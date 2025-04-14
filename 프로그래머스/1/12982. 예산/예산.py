def solution(d, budget):
    answer = 0
    #지원해줄 수 있는 최대 부서수 
    d.sort()
    
    for i in range(len(d)):
        if budget - d[i] >= 0:
            budget -= d[i]
            answer += 1
        else:
            break
    return answer