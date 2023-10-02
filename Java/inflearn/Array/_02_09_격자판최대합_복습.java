package Array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _02_09_격자판최대합_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        int rCross = 0;
        int lCross = 0;
        for (int i = 0; i < n; i++) {
            int rowSum = 0;
            int columnSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += arr[i][j];
                columnSum += arr[j][i];
                if (i == j) rCross += arr[i][j];
                if (i + j == n) lCross += arr[i][j];
            }
            answer = Math.max(answer, Math.max(rowSum, columnSum));
        }
        answer = Math.max(answer, Math.max(rCross, lCross));
        System.out.println(answer);
    }
}
