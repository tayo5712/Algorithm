package Array;

import java.util.Scanner;

public class _02_06_뒤집은소수_복습 {
    public static boolean isPrime(int num) {
        if (num == 1) return false;
        for (int i = 2; i < num/2; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String num = sc.next();
            int reverseNum = Integer.parseInt(new StringBuilder(num).reverse().toString());
            if (isPrime(reverseNum)) System.out.print(reverseNum + " ");
        }
    }
}
