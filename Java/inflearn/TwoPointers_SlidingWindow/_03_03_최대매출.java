package TwoPointers_SlidingWindow;

import java.util.Scanner;

public class _03_03_최대매출 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        int[] costs = new int[n];
        for (int i = 0; i < n; i++) {
            costs[i] = sc.nextInt();
        }
        int maxC = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (i < m) {
                sum += costs[i];
            }
            else {
                sum -= costs[i-m];
                sum += costs[i];
            }
            maxC = Math.max(maxC, sum);
        }
        System.out.println(maxC);
    }
}
