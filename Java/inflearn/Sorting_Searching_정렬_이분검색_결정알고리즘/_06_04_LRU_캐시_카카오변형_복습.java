package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class _06_04_LRU_캐시_카카오변형_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int m = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] move = new int[m];
        for (int i = 0; i < m; i++) {
            move[i] = Integer.parseInt(st.nextToken());
        }
        Stack<Integer> bag = new Stack<>();
        int result = 0;
        for (int i = 0; i < m; i++) {
            int pos = move[i]-1;
            for (int j = 0; j < n; j++) {
                // 크레인 내린 곳에 인형 찾기
                if (board[j][pos] != 0) {
                    // 인형이 있으면 bag 확인하기
                     if (!bag.isEmpty() && bag.peek() == board[j][pos]) {
                         // 뽑은 인형과 bag 상단 인형이 같은 인형일 때
                         bag.pop();
                         result += 2;
                     }
                     else {
                         // 같지 않으면 인형 넣기
                         bag.push(board[j][pos]);
                     }
                     // 뽑은 인형 없애주기
                     board[j][pos] = 0;
                     break;
                }
            }
        }
        System.out.println(result);
    }
}
