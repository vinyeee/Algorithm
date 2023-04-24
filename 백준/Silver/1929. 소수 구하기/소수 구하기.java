import java.util.*;

public class JV_1929_소수구하기 {

	public static void main(String[] args) {
		//에라토스테네스의 체
		
		Scanner sc = new Scanner(System.in);
		
		int M = sc.nextInt();
		int N = sc.nextInt(); 
		 
		int[] arr = new int[N+1];
		for(int i=0; i<arr.length; i++) {//배열에 0 ~ N까지의 수 저장
			arr[i] = i;
		}
		
		arr[1] = 0;
		
		for(int i = 2; i <= Math.sqrt(N); i++) {
			// 1은 모든 수의 약수이므로 1은 제외, 2부터 시작
			
			if(arr[i] == 0)continue;
			
			for(int j = i+i; j<=N; j=j+i) {
				arr[j] = 0;
			}
		}
		
		for(int i = M; i<= N; i++) {
			if(arr[i] != 0) {
				System.out.println(arr[i]);
			}
		}
	}

}
