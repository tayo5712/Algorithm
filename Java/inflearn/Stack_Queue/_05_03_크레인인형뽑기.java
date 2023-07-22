package Stack_Queue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class _05_03_크레인인형뽑기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] moves = new int[m];
        for (int i = 0; i < m; i++) {
            moves[i] = Integer.parseInt(st.nextToken());
        }
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        for (int i = 0; i < m; i++) {
            int pos = moves[i] - 1;
            for (int row = 0; row < n; row++) {
                if (board[row][pos] != 0) {
                    if (!stack.isEmpty() && stack.peek() == board[row][pos]) {
                        answer += 2;
                        stack.pop();
                    }
                    else {
                        stack.push(board[row][pos]);
                    }
                    board[row][pos] = 0;
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}
