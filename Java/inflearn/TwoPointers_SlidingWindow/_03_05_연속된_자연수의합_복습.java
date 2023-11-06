package TwoPointers_SlidingWindow;

import java.util.Scanner;

public class _03_05_연속된_자연수의합_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        int answer = 0;
        int st = 1;
        for (int i = 1; i <= n/2+1; i++) {
            sum += i;
            while (sum > n) {
                sum -= st++;
            }
            if (sum == n) {
                answer++;
            }
        }
        System.out.println(answer);
    }
}
