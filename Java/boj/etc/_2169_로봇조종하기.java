package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class _2169_로봇조종하기 {
    static int n, m, answer = 0;
    static int[][] arr;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int depth = 1;
        int[] topDP = new int[m];
        topDP[0] = arr[0][0];
        for (int i = 1; i < m; i++) {
            topDP[i] = arr[0][i] + topDP[i-1];
        }
        while (depth < n) {
            int[] leftDP = new int[m];
            leftDP[0] = topDP[0] + arr[depth][0];
            int[] rightDP = new int[m];
            rightDP[m-1] = topDP[m-1] + arr[depth][m-1];
            for (int i = 1; i < m; i++) {
                leftDP[i] = Math.max(leftDP[i-1], topDP[i]) + arr[depth][i];
                rightDP[m-(i+1)] = Math.max(rightDP[m-i], topDP[m-(i+1)]) + arr[depth][m-(i+1)];
            }
            for (int i = 0; i < m; i++) {
                topDP[i] = Math.max(leftDP[i], rightDP[i]);
            }
            depth++;
        }
        System.out.println(topDP[m-1]);
    }
}
