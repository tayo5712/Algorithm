package DynamicProgramming_동적계획법;

import java.util.ArrayList;
import java.util.Scanner;

public class _10_06_최대점수구하기_냅색알고리즘 {
    static class problem {
        int score;
        int time;
        public problem(int score, int time) {
            this.score = score;
            this.time = time;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<problem> problems = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            problems.add(new problem(a, b));
        }
        int[] dp = new int[m+1];
        for (int i = 0; i < n ; i++) {
            problem tmp = problems.get(i);
            for (int j = m; j >= tmp.time; j--) {
                dp[j] = Math.max(dp[j], dp[j - tmp.time] + tmp.score);
            }
        }
        System.out.println(dp[m]);
    }
}
