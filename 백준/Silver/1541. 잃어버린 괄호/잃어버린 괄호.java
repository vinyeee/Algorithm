

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String formula = sc.next();
		String[] for_arr = formula.split("\\-");
		
		int answer = 0;
		for(int i = 0; i<for_arr.length; i++) {
			int subAnswer = mySum(for_arr[i]);
			if(i == 0) {
				answer = subAnswer;
			}else {
				answer -= subAnswer;
			}
		}
		System.out.println(answer);
	}
	
	private static int mySum(String formula) {
		int partSum = 0;
		String[] subNumbers= formula.split("\\+");
		
		for(String subNumber : subNumbers) {
			partSum += Integer.parseInt(subNumber);
		}
		
		return partSum;
	}
	
}