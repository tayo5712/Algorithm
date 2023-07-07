package TwoPointers_SlidingWindow;

import java.util.Scanner;

public class _03_06_최대길이연속부분수열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int answer = 0;
        int lp = 0;
        int cnt = 0; // 0의 개수
        for (int rp = 0; rp < n; rp++) {
            if (arr[rp] == 0) cnt++;
            while (cnt > k) {
                if(arr[lp] == 0) cnt--;
                lp++;
            }
            answer = Math.max(answer, rp-lp+1);
        }
        System.out.println(answer);
    }
}
