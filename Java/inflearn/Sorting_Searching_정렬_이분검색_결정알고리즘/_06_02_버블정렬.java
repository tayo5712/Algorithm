package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.Scanner;

public class _06_02_버블정렬 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n - (i + 1); j++) {
                if (arr[j] > arr[j + 1]) {
                    int tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }
            }
        }
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
