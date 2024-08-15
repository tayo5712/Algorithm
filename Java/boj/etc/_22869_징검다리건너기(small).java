import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] stones = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            stones[i] = Integer.parseInt(st.nextToken());
        }
        Boolean[] dp = new Boolean[n+1];
        Arrays.fill(dp, false);
        dp[1] = true;
        for (int j = 2; j <= n; j++) {
            for (int i = 1; i < j ; i++) {
                if (dp[i] && (j-i)*(1+Math.abs(stones[i] - stones[j])) <= k) {
                    dp[j] = true;
                    break;
                }
            }
        }
        if (dp[n]) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
