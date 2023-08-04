package DFS_BFS;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class _08_13_섬나라아일랜드 {
    static int[][] world, visited;
    static int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};
    static int n = 0;
    static class point {
        int r;
        int c;
        public point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static void BFS(int r, int c) {
        Queue<point> q = new LinkedList<>();
        q.offer(new point(r, c));
        visited[r][c] = 1;
        while (!q.isEmpty()) {
            point cur = q.poll();
            for (int i = 0; i < 8; i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && world[nr][nc] == 1 && visited[nr][nc] == 0) {
                    visited[nr][nc] = 1;
                    q.offer(new point(nr, nc));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        n = sc.nextInt();
        world = new int[n][n];
        visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                world[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (world[i][j] == 1 && visited[i][j] == 0) {
                    BFS(i, j);
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}
