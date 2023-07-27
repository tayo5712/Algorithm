package DFS_BFS;

import java.util.ArrayList;
import java.util.Scanner;

public class _08_03_최대점수구하기 {
    static int answer = 0;
    static ArrayList<problem> arr;
    static int n, m;

    static class problem {
        int score;
        int time;
        public problem(int score, int time) {
            this.score = score;
            this.time = time;
        }
    }

    static public void DFS(int L, int time, int score) {
        if (time > m) return;
        if (L == n) {
            answer = Math.max(answer, score);
        } else {
            DFS(L + 1, time + arr.get(L).time, score + arr.get(L).score);
            DFS(L + 1, time, score);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            arr.add(new problem(a, b));
        }
        DFS(0, 0, 0);
        System.out.println(answer);
    }
}
