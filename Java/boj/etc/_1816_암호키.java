package etc;

import java.util.Scanner;

public class _1816_암호키 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            String answer = "YES";
            long num = sc.nextLong();
            for (long j = 2; j <= 1000000; j++) {
                if (num % j == 0) {
                    answer = "NO";
                    break;
                }
            }
            System.out.println(answer);
        }
    }
}
