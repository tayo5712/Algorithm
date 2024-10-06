package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.*;
import java.io.*;

public class _06_09_뮤직비디오_결정알고리즘_복습 {
    static int Count (int[] arr, int mid) {
        int cnt = 1;
        int sumV = 0;
        for (int i = 0; i < arr.length; i++) {
            if (sumV + arr[i] <= mid) sumV += arr[i];
            else {
                cnt++;
                sumV = arr[i];
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int answer = 0;
        int lt = Arrays.stream(arr).max().getAsInt();
        int rt = Arrays.stream(arr).sum();
        while (lt <= rt) {
            int mid = (lt + rt) / 2;
            if (Count(arr, mid) <= m) {
                answer = mid;
                rt = mid - 1;
            } else {
                lt = mid + 1;
            }
        }
        System.out.println(answer);
    }
}
