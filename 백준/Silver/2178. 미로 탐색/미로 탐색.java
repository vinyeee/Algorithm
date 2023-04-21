import java.util.*;

public class Main {
    static int[][] map;
    static boolean[][] visited;
    static int N, M;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        map = new int[N][M];
        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String str = sc.next();
            for (int j = 0; j < M; j++) {
                map[i][j] = str.charAt(j) - '0';
            }
        }

        int answer = bfs(0, 0);
        System.out.println(answer);
    }

    public static int bfs(int startX, int startY) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{startX, startY, 1});
        visited[startX][startY] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];

            if (x == N - 1 && y == M - 1) { // 목적지 도달
                return cnt;
            }

            for (int i = 0; i < 4; i++) { // 상하좌우 이동
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue; // 범위를 벗어남
                if (visited[nx][ny]) continue; // 이미 방문한 곳

                if (map[nx][ny] == 1) { // 이동 가능한 곳
                    q.offer(new int[]{nx, ny, cnt + 1});
                    visited[nx][ny] = true;
                }
            }
        }

        return -1; // 도달할 수 없는 경우
    }
}