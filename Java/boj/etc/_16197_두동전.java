
package etc;
import java.util.*;
import java.io.*;

public class _16197_두동전 {
    static int n = 0, m = 0;
    static Coin[] coins = new Coin[2];
    static char[][] board;
    static Boolean[][][][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new char[n][m];
        initBoolean();
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }
        int coinIdx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'o') {
                    coins[coinIdx++] = new Coin(i, j);
                }
            }
        }
        System.out.println(BFS());
    }
    private static class Coin {
        int r;
        int c;
        public Coin(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    private static class TwoCoins {
        int r1;
        int c1;
        int r2;
        int c2;
        int cnt;
        public TwoCoins(int r1, int c1, int r2, int c2, int cnt) {
            this.r1 = r1;
            this.c1 = c1;
            this.r2 = r2;
            this.c2 = c2;
            this.cnt = cnt;
        }
    }

    private static void initBoolean() {
        visited = new Boolean[n][m][n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < n; k++) {
                    Arrays.fill(visited[i][j][k], false);
                }
            }
        }
    }
    private static int BFS() {
        Queue<TwoCoins> myCoins = new LinkedList<>();
        myCoins.offer(new TwoCoins(coins[0].r, coins[0].c, coins[1].r, coins[1].c, 0));
        visited[coins[0].r][coins[0].c][coins[1].r][coins[1].c] = true;
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        while (!myCoins.isEmpty()) {
            TwoCoins curCoin = myCoins.poll();
            for (int i = 0; i < 4; i++) {
                int nr1 = curCoin.r1 + dr[i];
                int nc1 = curCoin.c1 + dc[i];
                int nr2 = curCoin.r2 + dr[i];
                int nc2 = curCoin.c2 + dc[i];
                int cnt = curCoin.cnt;
                if (cnt > 10) return -1;
                if (0 <= nr1 && nr1 < n && 0 <= nc1 && nc1 < m && 0 <= nr2 && nr2 < n && 0 <= nc2 && nc2 < m) {
                    if (board[nr1][nc1] == '#') {
                        nr1 = curCoin.r1;
                        nc1 = curCoin.c1;
                    }
                    if (board[nr2][nc2] == '#') {
                        nr2 = curCoin.r2;
                        nc2 = curCoin.c2;
                    }
                    if (!visited[nr1][nc1][nr2][nc2]) {
                        visited[nr1][nc1][nr2][nc2] = true;
                        myCoins.offer(new TwoCoins(nr1, nc1, nr2, nc2, cnt + 1));
                    }
                }
                else if ((0 <= nr1 && nr1 < n && 0 <= nc1 && nc1 < m) || (0 <= nr2 && nr2 < n && 0 <= nc2 && nc2 < m)) {
                    return cnt + 1;
                }
            }
        }
        return -1;
    }
}
