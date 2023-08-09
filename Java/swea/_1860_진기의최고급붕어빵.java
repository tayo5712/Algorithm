import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1860_진기의최고급붕어빵 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            String answer = "Possible";
            int[] customers = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                customers[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(customers);
            for (int i = 0; i < N; i++) {
                if ((customers[i] / M) * K - i <= 0) {
                    answer = "Impossible";
                    break;
                }
            }
            System.out.printf("#%d %s\n", tc, answer);
        }
    }
}
