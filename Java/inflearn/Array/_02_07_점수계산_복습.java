package Array;

import java.util.Scanner;

public class _02_07_점수계산_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        int score = 1;
        for (int i = 0; i < n; i++) {
            int result = sc.nextInt();
            if (result == 1) answer += score++;
            else score = 1;
        }
        System.out.println(answer);
    }
}
