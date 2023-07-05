package Array;

import java.util.Scanner;

public class _02_09_격자판최대합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int num = sc.nextInt();
                arr[i][j] = num;
            }
        }
        // 행
        int maxSum = 0;
        int rowSum = 0;
        int colSum = 0;
        for (int i = 0; i < n; i++) {
            int row = 0;
            int col = 0;
            for (int j = 0; j < n; j++) {
                row += arr[i][j];
                col += arr[j][i];
            }
            rowSum = Math.max(row, rowSum);
            colSum = Math.max(col, colSum);
        }
        maxSum = Math.max(rowSum, colSum);
        // 대각선
        int CrossR = 0;
        int CrossL = 0;
        for (int i = 0; i < n; i++) {
            CrossR += arr[i][i];
            CrossL += arr[i][n-i-1];
        }
        maxSum = Math.max(maxSum, Math.max(CrossL, CrossR));
        System.out.println(maxSum);
    }
}
