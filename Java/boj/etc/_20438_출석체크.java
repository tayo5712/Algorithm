
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] dp = new int[n + 3];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            int sleep_num = Integer.parseInt(st.nextToken());
            dp[sleep_num] = -1;
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            int qr_num = Integer.parseInt(st.nextToken());
            if (dp[qr_num] != -1) {
                int times = 2;
                for (int j = qr_num; j < n + 3; j = qr_num * times++) {
                    if (dp[j] == 0) {
                        dp[j] = 1;
                    }
                }
            }
        }
        int[] sum = new int[n + 3];
        for (int i = 3; i < n + 3; i++) {
            if (dp[i] == 0 || dp[i] == -1) {
                sum[i] = sum[i-1] + 1;
            } else {
                sum[i] = sum[i-1];
            }
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(sum[e] - sum[s-1]);
        }
    }
}
