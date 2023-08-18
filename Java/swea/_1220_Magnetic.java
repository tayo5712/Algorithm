import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1220_Magnetic {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int tc = 1; tc <= 10; tc++) {
            int n = Integer.parseInt(br.readLine());
            int[][] table = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    table[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            int answer = 0;
            for (int i = 0; i < n; i++) {
                int pre = 0;
                for (int j = 0; j < n; j++) {
                    if (table[j][i] == 1) {
                        pre = 1;
                    }
                    if (table[j][i] == 2 && pre == 1) {
                        answer += 1;
                        pre = 2;
                    }
                }
            }
            System.out.println("#" + tc + " " + answer);
        }
    }
}
