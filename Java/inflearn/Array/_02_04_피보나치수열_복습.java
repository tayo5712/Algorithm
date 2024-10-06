package Array;

import java.util.Scanner;

public class _02_04_피보나치수열_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] pibo = new int[n];
        pibo[0] = 1;
        pibo[1] = 1;
        System.out.print("1 1 ");
        for (int i = 2; i < n; i++) {
            pibo[i] = pibo[i - 2] + pibo[i - 1];
            System.out.print(pibo[i] + " ");
        }

    }
}
