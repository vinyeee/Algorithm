import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 정렬할 수 개수
		int[] arr = new int[N];
		
		for(int i=0; i<N; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);// 배열 정렬

		int M = sc.nextInt(); // 탐색할 수 개수
		
		for(int i=0; i<M; i++) {
			boolean find = false;
			int target = sc.nextInt();
			
			int start = 0;
			int end = N-1;
			while (start <= end) {
				int mid = (start + end) / 2;
				if(arr[mid] < target) {
					start = mid + 1;
				}else if(arr[mid] > target) {
					end = mid - 1;
				}else { // target == mid
					find = true;
					break;
				}
			}
			if(find == true) {
				System.out.println("1");
			}else {
				System.out.println("0");
			}
		}		

	}

}
