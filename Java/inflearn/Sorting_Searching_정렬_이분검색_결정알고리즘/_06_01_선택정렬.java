package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.Scanner;

public class _06_01_선택정렬 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = 0; i < n-1; i++) {
            int idx = i;
            for (int j = i+1; j < n; j++) {
                if (arr[idx] > arr[j]) idx = j;
            }
            int tmp = arr[idx];
            arr[idx] = arr[i];
            arr[i] = tmp;
        }
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
