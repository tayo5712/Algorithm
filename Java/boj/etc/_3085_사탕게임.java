package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _3085_사탕게임 {
    static int maxL = 0;
    static int n = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                char tmpR = board[i][j];
                char tmpD = board[j][i];
                // 오른쪽 교환

                char right = board[i][j + 1];
                board[i][j] = right;
                board[i][j + 1] = tmpR;
                Check(board);
                board[i][j] = tmpR;
                board[i][j + 1] = right;

                // 아래쪽 교환
                char down = board[j + 1][i];
                board[j][i] = down;
                board[j + 1][i] = tmpD;
                Check(board);
                board[j][i] = tmpD;
                board[j + 1][i] = down;

            }
        }
        System.out.println(maxL);
    }

    private static void Check(char[][] board) {
        for (int i = 0; i < n; i++) {
            int maxRight = 1;
            int maxDown = 1;
            for (int j = 1; j < n; j++) {
                if (board[i][j] == board[i][j - 1]) {
                    maxL = Math.max(++maxRight, maxL);
                } else if (board[i][j] != board[i][j - 1]) {
                    maxRight = 1;
                }

                if  (board[j][i] == board[j - 1][i]) {
                    maxL = Math.max(++maxDown, maxL);
                } else if (board[j][i] != board[j - 1][i]) {
                    maxDown = 1;
                }
            }
        }
    }
}
