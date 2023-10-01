package String;

import java.util.Scanner;

public class _01_10_문자거리_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char t = sc.next().charAt(0);
        int p = 101;
        int[] answer = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == t) {
                p = 0;
                answer[i] = p;
            }
            else {
                p += 1;
                answer[i] = p;
            }
        }

        p = 101;
        for (int i = s.length()-1; i > -1; i--) {
            if (s.charAt(i) == t) {
                p = 0;
            }
            else {
                p += 1;
                answer[i] = Math.min(answer[i], p);
            }
        }
        for (int i : answer) {
            System.out.print(i + " ");
        }
    }
}
