package DFS_BFS;

import java.util.Scanner;

public class _08_09_조합구하기 {
    static int[] combi;
    static int n, m;
    static void DFS(int L, int s) {
        if (L == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(combi[i] + " ");
            }
            System.out.println();
        }
        else {
            for (int i = s; i <= n; i++) {
                combi[L] = i;
                DFS(L + 1, i + 1);
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        combi = new int[m];
        DFS(0, 1);
    }
}
