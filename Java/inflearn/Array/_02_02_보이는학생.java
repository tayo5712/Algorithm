package Array;

import java.util.Scanner;

public class _02_02_보이는학생 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int cnt = 1;
        int tall = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > tall) {
                cnt++;
                tall = arr[i];
            }
        }
        System.out.println(cnt);
    }
}
