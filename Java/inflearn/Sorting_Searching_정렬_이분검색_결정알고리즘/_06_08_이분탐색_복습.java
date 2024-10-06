package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.Arrays;
import java.util.Scanner;

public class _06_08_이분탐색_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        int lt = 0, rt = n - 1;
        while (lt <= rt) {
            int mid = (lt + rt) / 2;
            if (arr[mid] == m) {
                System.out.println(mid + 1);
                break;
            } else if (arr[mid] > m) {
                rt = mid - 1;
            } else {
                lt = mid + 1;
            }
        }
    }
}
