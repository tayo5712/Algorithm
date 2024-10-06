package DFS_BFS;

import java.util.Scanner;

public class _08_01_합이같은부분집합_복습 {
    static int total = 0;
    static int n = 0;
    static String answer = "NO";
    static int[] arr;
    static boolean flag = false;
    static void group(int idx, int sumV) {
        if (flag) return;
        if (sumV > total / 2) return;
        if (idx == n) {
            if ((total - sumV) == sumV) {
                answer = "YES";
                flag = true;
                return;
            }
        } else {
            group(idx + 1, sumV);
            group(idx + 1, sumV + arr[idx]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            total += arr[i];
        }
        group(0, 0);
        System.out.println(answer);
    }
}
