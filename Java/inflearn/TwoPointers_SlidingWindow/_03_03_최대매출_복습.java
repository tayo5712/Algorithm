package TwoPointers_SlidingWindow;

import java.util.Scanner;

public class _03_03_최대매출_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int answer = 0;
        for (int i = 0; i < k; i++) {
            answer += arr[i];
        }
        int sum = answer;
        for (int i = 1; i < n-k; i++) {
            sum -= arr[i-1];
            sum += arr[i+k-1];
            answer = Math.max(answer, sum);
        }
        System.out.println(answer);
    }
}
