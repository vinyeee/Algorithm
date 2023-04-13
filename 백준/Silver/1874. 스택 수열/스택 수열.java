import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int A[] = new int[N];
		
		for(int i = 0; i < N; i++) {
			A[i] =  sc.nextInt();//배열에 수열을 저장
		}// 배열에 저장된 수를 하나씩 꺼내오는 변수를 su라 하겠음
		
		int num = 1;
		Stack<Integer> stack = new Stack<>();
		StringBuffer bf = new StringBuffer();
		boolean result = true;
		for(int i = 0; i < N; i++) { //수 하나에 대해
			int su = A[i];
			if(su >= num) {
				while(su >= num) {
					stack.push(num++);
					bf.append("+\n");
				}
				stack.pop();
				bf.append("-\n");
			}else {
				if(su < stack.peek()) {
					System.out.println("NO");
					result = false;
					break;
				}else {
					stack.pop();
					bf.append("-\n");
				}
				
			}
		}
		if (result) System.out.println(bf.toString());
	}

}
