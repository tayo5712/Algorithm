package DynamicProgramming_동적계획법;

import java.util.Arrays;
import java.util.Scanner;

public class _10_05_동전교환_냅색알고리즘 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }
        int total = sc.nextInt();
        int dp[] = new int[total+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i < total+1; i++) {
                dp[i] = Math.min(dp[i - coin] + 1, dp[i]);
            }
        }
        System.out.println(dp[total]);
    }
}
