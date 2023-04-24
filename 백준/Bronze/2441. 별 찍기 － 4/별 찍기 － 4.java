import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for(int i = 0; i<N; i++) {
			for(int j = 0; j<i; j++) {
				System.out.print(" ");//i만큼 공백을 찍고 별은 n-i개
			}
			for(int k = 0; k < N-i; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
	
}
