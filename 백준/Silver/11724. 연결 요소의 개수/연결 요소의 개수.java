import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer>[] adjList;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 정점의 개수
        int m = sc.nextInt(); // 간선의 개수

        // 인접 리스트 초기화
        adjList = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            adjList[i] = new ArrayList<Integer>();
        }

        // 그래프 생성
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adjList[u].add(v);
            adjList[v].add(u);
        }

        // 방문 여부 배열 초기화
        visited = new boolean[n + 1];

        int count = 0;
        // 모든 정점에 대하여 DFS 탐색
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                count++;
                dfs(i);
            }
        }

        // 연결 요소의 개수 출력
        System.out.println(count);
    }

    // 깊이 우선 탐색(DFS)
    private static void dfs(int vertex) {
        visited[vertex] = true;
        for (int adjVertex : adjList[vertex]) {
            if (!visited[adjVertex]) {
                dfs(adjVertex);
            }
        }
    }
}