package Array;

import java.util.Scanner;

public class _02_01_큰수출력하기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.print(arr[0] + " ");
        for (int i = 1; i < n; i++) {
            if (arr[i-1] < arr[i]) {
                System.out.print(arr[i] + " ");
            }
        }
    }
}
