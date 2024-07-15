import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] music = new long[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        music[1] = Long.parseLong(st.nextToken());
        int[] dp = new int[n + 1];
        for (int i = 2; i < n + 1; i++) {
            music[i] = Long.parseLong(st.nextToken());
            if (music[i] < music[i-1]) {
                dp[i] = dp[i-1] + 1;
            } else {
                dp[i] = dp[i-1];
            }
        }
        int q = Integer.parseInt(br.readLine());
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(dp[e] - dp[s]);
        }
    }
}
