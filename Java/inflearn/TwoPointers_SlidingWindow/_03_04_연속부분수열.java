package TwoPointers_SlidingWindow;

import java.util.Scanner;

public class _03_04_연속부분수열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int answer = 0, sum = 0, lt = 0;
        for (int rt = 0; rt < n; rt++) {
            sum += arr[rt];
            if (sum == m) answer++;
            while (sum >=m) {
                sum -= arr[lt++];
                if (sum == m)  answer++;
            }
        }
        System.out.println(answer);


//        int answer = 0;
//        int lp = 0;
//        int rp = 0;
//        int sum = arr[rp];
//        while (rp < n) {
//            if (sum == m) {
//                answer++;
//                rp++;
//                if (rp >=n) break;
//                sum += arr[rp];
//                sum -= arr[lp++];
//            } else if (sum < m) {
//                rp++;
//                if (rp >=n) break;
//                sum += arr[rp];
//            } else {
//                sum -= arr[lp++];
//            }
//        }
//        System.out.println(answer);
    }
}
