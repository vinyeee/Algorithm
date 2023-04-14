

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Queue<Integer> que = new LinkedList<>();
		
		for(int i = 1; i < N+1; i++ ) {
			que.add(i);
		}
		
		
		for(int i = 0; i < N-1; i++) {
			que.poll();
			int n = que.poll();
			que.add(n);
		}
		System.out.println(que.poll());
	}

}
