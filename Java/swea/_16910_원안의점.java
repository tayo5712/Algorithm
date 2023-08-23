import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _16910_원안의점 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc < T + 1; tc++) {
            int n = Integer.parseInt(br.readLine());
            int cnt = 0;
            for (int x = -n; x <= n; x++) {
                for (int y = -n; y <= n; y++) {
                    if ((x*x) + (y*y) <= n*n) cnt++;
                }
            }
            System.out.println("#" + tc + " " + cnt);
        }
    }
}
