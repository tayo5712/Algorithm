package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _3108_빵집 {
    static char[][] map;
    static int n, m, answer = 0;
    static int[] dr = {-1, 0, 1};
    static boolean flag = true;
    static void DFS(int r, int c) {
        if (!flag) return;
        if (c == m-1) {
            answer++;
            flag = false;
        }
        else {
            for (int i = 0; i < 3; i++) {
                int nr = r + dr[i];
                if (0 <= nr && nr < n && map[nr][c+1] == '.' && flag == true) {
                    map[nr][c+1] = '-';
                    DFS(nr, c+1);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new char[n][];
        for (int i = 0; i < n; i++) {
            map[i] = br.readLine().toCharArray();
        }
        for (int i = 0; i < n; i++) {
            flag = true;
            DFS(i, 0);
        }
        System.out.println(answer);
    }
}
