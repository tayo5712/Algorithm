package Array;

import java.util.Scanner;

public class _02_08_등수구하기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int result[] = new int[n];
        for (int i = 0; i < n; i++) {
            int rank = 1;
            for (int j = 0; j < n; j++) {
                if (arr[i] < arr[j]) rank++;
            }
            result[i] = rank;
        }

        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}
