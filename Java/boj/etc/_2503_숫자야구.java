package etc;

import java.util.ArrayList;
import java.util.Scanner;

public class _2503_숫자야구 {
    static class hint {
        int num;
        int str;
        int ball;
        public hint(int num, int str, int ball) {
            this.num = num;
            this.str = str;
            this.ball = ball;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        ArrayList<hint> hints = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            int str = sc.nextInt();
            int ball = sc.nextInt();
            hints.add(new hint(num, str, ball));
        }
        for (int i = 1; i < 10; i++) {
            for (int j = 1; j < 10; j++) {
                for (int k = 1; k < 10; k++) {
                    if (i == j || i == k || j == k) continue;
                    int cnt = 0;
                    for (hint h : hints) {
                        int curStr = 0;
                        int curBall = 0;

                        int first = h.num / 100;
                        int second = (h.num - first * 100) / 10;
                        int third = (h.num - (first * 100) - (second * 10));

                        if (i == first) curStr++;
                        if (j == second) curStr++;
                        if (k == third) curStr++;
                        if (i == second || i == third) curBall++;
                        if (j == first || j == third) curBall++;
                        if (k == first || k == second) curBall++;

                        if (curStr == h.str && curBall == h.ball) cnt++;
                    }
                    if (cnt == n) answer++;
                }
            }
        }
        System.out.println(answer);
    }
}
