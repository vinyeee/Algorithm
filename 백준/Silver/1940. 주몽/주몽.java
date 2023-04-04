

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); 
		
		int N = sc.nextInt(); // 재료의 개수 
		int M = sc.nextInt(); // 갑옷이 되는 번호 
		
		int [] arr = new int[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr); //배열을 오름차순으로 정렬 
		
		int i = 0,count = 0;
		int j = N - 1;
		
		while(i < j) {
			if(arr[i] + arr[j] > M) j--;
			else if(arr[i] + arr[j] < M) i++;
			else {count++; i++; j--;}
		}
		
		System.out.println(count);
		
	}

}
