package etc;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _1303_전쟁_전투 {
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int[] answer = {0 ,0};
    static int n;
    static int m;
    static int[][] visited;

    static String[][] arr;

    static class Pos {
        int r;
        int c;

        Pos(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    static void BFS(int r, int c, int n, int m, String nowTeam) {
        int cnt = 1;
        Queue<Pos> q = new LinkedList<>();
        q.offer(new Pos(r, c));
        while (!q.isEmpty()) {
            Pos nowPos = q.poll();
            int nowR = nowPos.r;
            int nowC = nowPos.c;
            for (int i = 0; i < 4; i++) {
                int nextR = nowR + dr[i];
                int nextC = nowC + dc[i];
                if (nextR >= 0 && nextR < n && nextC >= 0 && nextC < m && nowTeam.equals(arr[nextR][nextC]) && visited[nextR][nextC] == 0) {
                    visited[nextR][nextC] = 1;
                    cnt++;
                    q.offer(new Pos(nextR, nextC));
                }
            }
        }

        if (nowTeam.equals("W")) {
            answer[0] += cnt * cnt;
        } else {
            answer[1] += cnt * cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        arr = new String[n][m];
        visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            arr[i] = s.split("");
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] == 0) {
                    visited[i][j] = 1;
                    BFS(i, j, n, m, arr[i][j]);
                }
            }
        }

        System.out.println(answer[0] + " " + answer[1]);
    }
}
