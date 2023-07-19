package DynamicProgramming_동적계획법;

import java.util.Scanner;

public class _10_02_돌다리건너기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dp = new int[n+2];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < n + 2; i++) {
            dp[i] = dp[i - 2] + dp[i - 1];
        }
        System.out.println(dp[n+1]);
    }
}
