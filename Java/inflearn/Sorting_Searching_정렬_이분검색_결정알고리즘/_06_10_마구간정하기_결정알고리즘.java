package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.Arrays;
import java.util.Scanner;

public class _06_10_마구간정하기_결정알고리즘 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        int answer = 0;
        int lt = 1;
        int rt = arr[n-1];
        while (lt <= rt) {
            int mid = (lt + rt) / 2;
            int cnt = 1;
            int ep = 0;
            for (int i = 0; i < n; i++) {
                if (arr[i] - arr[ep] >= mid) {
                    cnt++;
                    ep = i;
                }
            }
            if (cnt >= m) {
                answer = Math.max(answer, mid);
                lt = mid + 1;
            }
            else rt = mid - 1;
        }
        System.out.println(answer);
    }
}
