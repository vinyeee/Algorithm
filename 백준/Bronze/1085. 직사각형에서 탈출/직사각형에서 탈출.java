
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		int w = sc.nextInt();
		int h = sc.nextInt();
		int w_x = w-x;
		int h_y = h-y;
		
		int[] arr = {x,y,w_x,h-y};
		Arrays.sort(arr);
		System.out.println(arr[0]);
		
	}
	
}