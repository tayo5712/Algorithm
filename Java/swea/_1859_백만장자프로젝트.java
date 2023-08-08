import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1859_백만장자프로젝트 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc < T + 1; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            long answer = 0;
            int maxV = 0;
            for (int i = N - 1; i >= 0 ; i--) {
                if (arr[i] > maxV) maxV = arr[i];
                else answer += maxV - arr[i];
            }
            System.out.println("#" + tc + " " + answer);
        }
    }
}
