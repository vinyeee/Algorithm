
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Scanner sc = new Scanner(System.in);
		 int n = sc.nextInt();
		 
		 long sum = 0;
		 long max = 0;
		 
		 for(int i=0; i<n; i++) {
			 int tmp = sc.nextInt();
			 if(tmp > max) {
				 max = tmp;
			 }
			 sum += tmp;
		 }
		 
		 System.out.println(sum * 100.0 / max / n);
		 
		  // ex) N = 3 이고 , 최댓값을 M 이라 하면 
	        // = (A/M * 100.0 + B/M * 100 + c/M * 100)/N
	        // = ((A+B+C) * 100.0/M) / N
	        // = (A+B+C) * 100.0 / M / N
		
	}

}