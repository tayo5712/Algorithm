package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.Scanner;

public class _06_03_삽입정렬 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 1; i < n; i++) {
            int tmp = arr[i], j;
            for (j = i-1; j >= 0 ; j--) {
                if (arr[j] > tmp) arr[j + 1] = arr[j];
                else break;
            }
            arr[j+1] = tmp;
        }
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
