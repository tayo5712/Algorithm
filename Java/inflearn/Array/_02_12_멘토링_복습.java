package Array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _02_12_멘토링_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        for (int i = 1; i < m + 1; i++) {
            int[] check = new int[m];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    check[arr[j][k] - 1] = 1;
                    if (arr[j][k] == i) break;
                }
            }

            for (int j = 0; j < m; j++) {
                if (check[j] == 0) answer++;
            }
        }
        System.out.println(answer);
    }
}
