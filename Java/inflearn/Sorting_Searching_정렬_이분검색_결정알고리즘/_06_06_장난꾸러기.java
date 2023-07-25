package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.Arrays;
import java.util.Scanner;

public class _06_06_장난꾸러기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int[] tmp = arr.clone();
        Arrays.sort(tmp);
        int A = 0, B = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] != tmp[i]) {
                if (A == 0) A = i + 1;
                else B = i + 1;
            }
        }
        System.out.println(A + " " + B);
    }
}
