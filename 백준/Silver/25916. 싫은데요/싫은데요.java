import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // N개의 구멍
        int M = sc.nextInt(); // 햄스터의 부피 M

        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int i = 0;
        int j = 0;
        int sum = arr[0], max = 0; // max 초기값은 0

        while (j < N) {
            if (sum <= M) { // sum이 M과 같을 때도 처리해야 함
                if (sum > max) max = sum; // 최대값 갱신
                j++;
                if (j < N) {
                    sum += arr[j];
                }
            } else {
                sum -= arr[i];
                i++;
            }
        }
        System.out.println(max);
    }
}