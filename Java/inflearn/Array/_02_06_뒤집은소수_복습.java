package Array;

import java.util.Scanner;

public class _02_06_뒤집은소수_복습 {
    static void isPrime(int num) {
        if (num == 1) return;
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return;
            }
        }
        System.out.print(num + " ");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            isPrime(Integer.parseInt(String.valueOf(new StringBuilder(sc.next()).reverse())));
        }
    }
}
