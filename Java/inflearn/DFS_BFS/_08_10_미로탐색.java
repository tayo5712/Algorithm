package DFS_BFS;

import java.util.Scanner;

public class _08_10_미로탐색 {
    static int answer = 0;
    static int[][] miro = new int[7][7];
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};
    static int[][] visited = new int[7][7];
    public void DFS(int r, int c) {
        if (r == 6 && c == 6) {
            answer++;
            return;
        }
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (0 <= nr && nr < 7 && 0 <= nc && nc < 7 && miro[nr][nc] == 0 && visited[nr][nc] == 0) {
                visited[nr][nc] = 1;
                DFS(nr, nc);
                visited[nr][nc] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                miro[i][j] = sc.nextInt();
            }
        }
        _08_10_미로탐색 T = new _08_10_미로탐색();
        visited[0][0] = 1;
        T.DFS(0, 0);
        System.out.println(answer);
    }
}
