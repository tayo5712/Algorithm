package DFS_BFS;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class _08_12_토마토 {
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, -1, 0, 1};
    static int[][] box, dis;
    static Queue<tomato> tomatoes;
    static int n, m = 0;
    static class tomato {
        int r;
        int c;
        public tomato(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static void BFS() {
        while (!tomatoes.isEmpty()) {
            tomato t = tomatoes.poll();
            for (int j = 0; j < 4; j++) {
                int nr = t.r + dr[j];
                int nc = t.c + dc[j];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && box[nr][nc] == 0) {
                    box[nr][nc] = 1;
                    tomatoes.offer(new tomato(nr, nc));
                    dis[nr][nc] = dis[t.r][t.c] + 1;
                }
            }
        }
    }

    static int Check() {
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (box[i][j] == 0) return -1;
                answer = Math.max(answer, dis[i][j]);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        m = sc.nextInt();
        n = sc.nextInt();
        tomatoes = new LinkedList<>();
        box = new int[n][m];
        dis = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                box[i][j] = sc.nextInt();
                if (box[i][j] == 1) {
                    tomatoes.offer(new tomato(i, j));
                }
            }
        }
        BFS();
        System.out.println(Check());


    }
}
