import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine(); // 버퍼 비우기

        for (int i = 1; i <= n; i++) {
            String line = sc.nextLine();
            String[] words = line.split(" ");
            System.out.printf("Case #%d: ", i);
            for (int j = words.length - 1; j >= 0; j--) {
                System.out.print(words[j]);
                if (j > 0) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        sc.close();
    }
}