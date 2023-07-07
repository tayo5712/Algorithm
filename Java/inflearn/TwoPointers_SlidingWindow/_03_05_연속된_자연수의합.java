package TwoPointers_SlidingWindow;

import java.util.Scanner;

public class _03_05_연속된_자연수의합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        int answer = 0;
        int lp = 1;
        for (int rp = 1; rp < n/2+2; rp++) {
            sum += rp;
            if (sum == n) {
                answer++;
            }
            while (sum >= n) {
                sum -= (lp++);
                if (sum == n) answer++;
            }
        }
        System.out.println(answer);
    }
}
