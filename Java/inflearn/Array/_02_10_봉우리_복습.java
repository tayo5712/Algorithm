package Array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _02_10_봉우리_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n + 2][n + 2];
        for (int i = 1; i < n + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n + 1; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int ans = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (arr[i][j] > arr[i - 1][j] &&
                        arr[i][j] > arr[i + 1][j] &&
                        arr[i][j] > arr[i][j - 1] &&
                        arr[i][j] > arr[i][j + 1]) {
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }
}
