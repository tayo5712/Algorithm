package DFS_BFS;

import java.util.ArrayList;
import java.util.Scanner;

// 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
public class _08_04_중복순열 {
    static int n, m = 0;
    static int[] pm;
    static void DFS(int L) {
        if (L == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(pm[i] + " ");
            }
            System.out.println();
        }
        else {
            for (int i = 1; i <= n ; i++) {
                pm[L] = i;
                DFS(L+1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        pm = new int[m];
        DFS(0);
    }
}
