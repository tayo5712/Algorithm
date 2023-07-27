package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.Arrays;
import java.util.Scanner;

public class _06_09_뮤직비디오_결정알고리즘 {
    public int count(int[] arr, int capacity) {
        int cnt = 1;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            if (sum + arr[i] > capacity) {
                cnt++;
                sum = arr[i];
            } else {
                sum += arr[i];
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        _06_09_뮤직비디오_결정알고리즘 T = new _06_09_뮤직비디오_결정알고리즘();
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
            int mid = (lt+rt)/2;
            if (T.count(arr, mid) <= m) {
                answer = mid;
                rt = mid-1;
            } else lt = mid + 1;
        }
        System.out.println(answer);
    }
}
