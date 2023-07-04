package Array;

import java.util.Scanner;

public class _02_07_점수계산 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int score = 0;
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 1) {
                score++;
                result += score;
            } else {
                score = 0;
            }
        }
        System.out.println(result);
    }
}
