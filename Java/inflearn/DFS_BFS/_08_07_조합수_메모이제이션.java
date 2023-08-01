package DFS_BFS;

import java.util.Scanner;

public class _08_07_조합수_메모이제이션 {
    static int[][] memo;
    static int DFS(int n, int r) {
        if (memo[n][r] != 0) return memo[n][r];
        if (n == r || r == 0) return 1;
        else return memo[n][r] = DFS(n-1, r-1) + DFS(n-1, r);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r = sc.nextInt();
        memo = new int[n+1][r+1];
        System.out.println(DFS(n, r));
    }
}
