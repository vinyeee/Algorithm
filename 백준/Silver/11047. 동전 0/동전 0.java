import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); //동전의 개수
		int k = sc.nextInt(); //목표 금액
		int[] coins = new int[N];
		
		for(int i=0; i<N; i++) {
			coins[i] = sc.nextInt();
		}// 동전 배열에 값 저장
		
		int cnt = 0;
		for(int i=N-1; i>=0; i--) {
			if(coins[i] <= k) {// 목표 금액보다 동전 값이 더 작으면
				cnt += k / coins[i];
				k = k % coins[i];
			}
		}
		
		System.out.println(cnt);

	}

}
