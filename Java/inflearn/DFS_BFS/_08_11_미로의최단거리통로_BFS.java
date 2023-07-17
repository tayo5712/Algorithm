package DFS_BFS;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Point {
    public int r, c;
    public int cnt;

    Point(int r, int c, int cnt) {
        this.r = r;
        this.c = c;
        this.cnt = cnt;
    }
}

public class _08_11_미로의최단거리통로_BFS {

    public int BFS(int[][] miro) {
        Queue<Point> q = new LinkedList<>();
        int[][] visited = new int[7][7];
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, -1, 0, 1};
        Point p = new Point(0, 0, 0);
        visited[0][0] = 1;
        q.offer(p);
        while (!q.isEmpty()) {
            Point myP = q.poll();
            for (int i = 0; i < 4; i++) {
                int nr = myP.r + dr[i];
                int nc = myP.c + dc[i];
                if (nr == 6 && nc == 6) return myP.cnt + 1;
                if (0 <= nr && nr < 7 && 0 <= nc && nc < 7 && visited[nr][nc] == 0 && miro[nr][nc] == 0) {
                    visited[nr][nc] = 1;
                    Point np = new Point(nr, nc, myP.cnt + 1);
                    q.offer(np);
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] miro = new int[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                miro[i][j] = sc.nextInt();
            }
        }
        _08_11_미로의최단거리통로_BFS T = new _08_11_미로의최단거리통로_BFS();
        System.out.println(T.BFS(miro));
    }
}
