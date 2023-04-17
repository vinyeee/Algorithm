
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		//자릿수 정렬
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		int A[] = new int[str.length()];
		for(int i = 0; i<str.length();i++) {
			A[i] = Integer.parseInt(str.substring(i,i+1));
		}
		// 선택 정렬
		for(int i = 0; i<str.length(); i++) {
			int Max = i; // 가장 첫 번째 원소
			for (int j = i+1; j<str.length(); j++) {
				if(A[j]>A[Max]) {
					Max = j;	
				}
			}if(A[i] < A[Max]) {
				int tmp = A[i];
				A[i] = A[Max];
				A[Max] = tmp; 
			}
		}
		for(int i = 0; i<A.length; i++) {
			System.out.print(A[i]);
		}
	}

}