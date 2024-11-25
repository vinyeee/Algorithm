# 입력 받기
n, t = map(int, input().split())  # 그리드 크기 n과 시간 t 입력
r, c, d = input().split()         # 초기 위치 r, c와 방향 d 입력
r = int(r)
c = int(c)

# 방향에 따른 이동 좌표 설정
direction_map = {
    'U': (-1, 0),  # 위
    'D': (1, 0),   # 아래
    'L': (0, -1),  # 왼쪽
    'R': (0, 1)    # 오른쪽
}

# 현재 방향의 행과 열 변화량
dr, dc = direction_map[d]

# t초 동안 시뮬레이션
for _ in range(t):
    # 다음 위치 계산
    nr = r + dr
    nc = c + dc
    
    # 다음 위치가 그리드 내에 있는지 확인
    if 1 <= nr <= n and 1 <= nc <= n:
        # 그리드 내에 있으면 이동
        r, c = nr, nc
    else:
        # 그리드 밖이면 방향 반전
        dr, dc = -dr, -dc

# 최종 위치 출력
print(r, c)