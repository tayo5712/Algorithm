package TwoPointers_SlidingWindow;

import java.util.*;

public class _03_01_두배열합치기 {
    public static void main(String[] args) {
    // 1 투포인터
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr1 = new int[n];
        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }

        int m = sc.nextInt();
        int[] arr2 = new int[m];
        for (int i = 0; i < m; i++) {
            arr2[i] = sc.nextInt();
        }

        ArrayList answer = new ArrayList<>();
        int a = 0;
        int b = 0;

        while (a < n && b < m) {
            if (arr1[a] < arr2[b]) {
                answer.add(arr1[a]);
                a++;
            } else {
                answer.add(arr2[b]);
                b++;
            }
        }

        if (a >= n) {
            while (b < m) {
                answer.add(arr2[b]);
                b++;
            }
        }
        else if (b >= m) {
            while (a < n) {
                answer.add(arr1[a]);
                a++;
            }
        }

        for (int j = 0; j < answer.size(); j++) {
            System.out.print(answer.get(j) + " ");
        }


        // 2 그냥 합치고 정렬
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[] arr1 = new int[n];
//        for (int i = 0; i < n; i++) {
//            arr1[i] = sc.nextInt();
//        }
//        int m = sc.nextInt();
//        int[] arr2 = new int[m];
//        for (int i = 0; i < m; i++) {
//            arr2[i] = sc.nextInt();
//        }
//        int answer[] = new int[n + m];
//        for (int i = 0; i < n + m; i++) {
//            if (i < n) {
//                answer[i] = arr1[i];
//            } else {
//                answer[i] = arr2[i - n];
//            }
//        }
//        Arrays.sort(answer);
//        for (int i = 0; i < n + m; i++) {
//            System.out.print(answer[i] + " ");
//        }
    }
}
