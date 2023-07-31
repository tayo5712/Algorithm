package DFS_BFS;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class _08_05_동전교환 {
    static Integer[] coins;
    static int n, m = 0;
    static int answer = Integer.MAX_VALUE;
    static void DFS(int sum, int num) {
        if (sum > m) return;
        if (num >= answer) return;
        if (sum == m) {
            answer = Math.min(answer, num);
        }
        else {
            for (int i = 0; i < n; i++) {
                DFS(sum + coins[i], num + 1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        coins = new Integer[n];
        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }
        Arrays.sort(coins, Collections.reverseOrder()); // Collections 쓰러면 Integer
        m = sc.nextInt();
        DFS(0, 0);
        System.out.println(answer);
    }
}
