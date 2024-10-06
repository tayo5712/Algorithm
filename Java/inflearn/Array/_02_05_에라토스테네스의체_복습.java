package Array;

import java.util.Scanner;

public class _02_05_에라토스테네스의체_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] sosu = new int[n + 1];
        int ans = 0;
        for (int i = 2; i < n + 1; i++) {
            if (sosu[i] == 0) {
                ans++;
                for (int j = i; j < n + 1; j += i) {
                    sosu[j] = 1;
                }
            }
        }
        System.out.println(ans);
    }
}
