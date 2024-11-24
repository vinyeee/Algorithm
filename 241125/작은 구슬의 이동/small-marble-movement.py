import sys
input = sys.stdin.readline

# 입력 받기
n, t = map(int, input().split())
r, c, d = map(str, input().split())
r, c = int(r), int(c)

# 방향 설정 (R, D, U, L)
dy = [0, -1, 1, 0]  # 오른쪽, 위쪽, 아래쪽, 왼쪽
dx = [1, 0, 0, -1]

# 범위 체크 함수
def in_range(ny, nx):
    return 1 <= ny <= n and 1 <= nx <= n

# 방향을 숫자로 매핑 (R=0, D=1, U=2, L=3)
mapper = {'R': 0, 'D': 1, 'U': 2, 'L': 3}
move_dir = mapper[d]  # 초기 방향

# t초 동안 구슬 이동
for _ in range(t):
    ny, nx = r + dy[move_dir], c + dx[move_dir]  # 다음 좌표 계산
    if in_range(ny, nx):  # 벽에 부딪히지 않으면
        r, c = ny, nx  # 이동
    else:  # 벽에 부딪히면
        move_dir = 3 - move_dir  # 반대 방향으로 전환
        # 1초 후 방향 전환이 이루어지므로, 그 후 이동
    

# 결과 출력
print(r, c)

