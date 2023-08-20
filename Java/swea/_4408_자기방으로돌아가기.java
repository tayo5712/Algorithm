import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _4408_자기방으로돌아가기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] bokdo = new int[201];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int nowRoom = Integer.parseInt(st.nextToken());
                int returnRoom = Integer.parseInt(st.nextToken());
                nowRoom++;
                returnRoom++;
                if (nowRoom < returnRoom) {
                    for (int path = nowRoom/2; path <= returnRoom/2; path++) bokdo[path] += 1;
                } else {
                    for (int path = returnRoom/2; path <= nowRoom/2; path++) bokdo[path] += 1;
                }
            }
            int answer = 0;
            for (int i = 1; i < 201; i++) {
                if (bokdo[i] > answer) answer = bokdo[i];
            }
            System.out.println("#" + tc + " " + answer);
        }
    }
}
