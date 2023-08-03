package DFS_BFS;

import java.sql.SQLOutput;
import java.util.Scanner;

public class _08_08_수열추측하기 {
    static int n, k = 0;
    static int[] ch, com, visited;
    static int[][] memo;
    static boolean flag = false;
    static int COM(int n, int r) {
        if (memo[n][r] != 0) return memo[n][r];
        if (n == r || r == 0) return 1;
        else return memo[n][r] = COM(n-1, r-1) + COM(n-1, r);
    }

    static void DFS(int L, int sum) {
        if (sum > k || flag == true) return;
        if (L == n) {
            if (sum == k) {
                for (int i = 0; i < n; i++) {
                    System.out.print(ch[i] + " ");
                }
                flag = true;
            }
        }
        else {
            for (int i = 1; i <= n; i++) {
                if (visited[i] == 0) {
                    ch[L] = i;
                    visited[i] = 1;
                    DFS(L+1, sum + (com[L] * ch[L]));
                    visited[i] = 0;
                }
            }
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        ch = new int[n];
        com = new int[n];
        visited = new int[n+1];
        memo = new int[n+1][n+1];
        for (int i = 0; i < n; i++) {
            com[i] = COM(n-1, i);
        }
        DFS(0, 0);
    }
}
