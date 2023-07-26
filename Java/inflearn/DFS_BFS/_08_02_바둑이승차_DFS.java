package DFS_BFS;

import java.util.Scanner;

public class _08_02_바둑이승차_DFS {
    static int answer = 0;
    static int[] arr;
    static int c = 0, n = 0;
    public void DFS(int L, int sumV) {
        if (sumV > c) return;
        if (L == n) {
            answer = Math.max(answer, sumV);
        }
        else {
            DFS(L + 1, sumV + arr[L]);
            DFS(L + 1, sumV);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        c = sc.nextInt();
        n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        _08_02_바둑이승차_DFS T = new _08_02_바둑이승차_DFS();
        T.DFS(0, 0);
        System.out.println(answer);
    }
}
