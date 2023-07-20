package DynamicProgramming_동적계획법;

import java.util.Scanner;

public class _10_03_최대부분증가수열_LIS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dp = new int[n];
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        dp[0] = 1;
        int maxV = 0;
        for (int i = 1; i < n; i++) {
            dp[i] = 1;
            for (int j = i - 1; j >= 0; j--) {
                if (arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxV = Math.max(maxV, dp[i]);
        }
        System.out.println(maxV);
    }
}
