def solution(citations):
    
    citations.sort(reverse = True)
    
    # 각 인용 수를 순회하면서 H-Index 조건 확인
    for i, c in enumerate(citations):
        # i는 현재까지의 논문 개수 (0부터 시작하므로 +1 필요)
        if i + 1 > c:
            return i  # 조건이 깨지는 순간, 직전 i가 최대 H-Index
    
    # 모든 논문이 인용 수가 충분한 경우, 전체 개수가 H-Index
    return len(citations)