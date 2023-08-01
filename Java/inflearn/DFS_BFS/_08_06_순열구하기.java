package DFS_BFS;

import java.util.Scanner;

public class _08_06_순열구하기 {
    static int n, m = 0;
    static int[] arr, answer, visited;
    static void DFS(int L) {
        if (L == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(answer[i] + " ");
            }
            System.out.println();
        }
        else {
            for (int i = 0; i < n; i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    answer[L] = arr[i];
                    DFS(L + 1);
                    visited[i] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        visited = new int[n];
        answer = new int[m];
        DFS(0);
    }
}
