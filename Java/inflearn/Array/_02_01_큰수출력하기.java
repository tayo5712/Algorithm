package Array;

import java.util.ArrayList;
import java.util.Scanner;

public class _02_01_큰수출력하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        // 1
        ArrayList<Integer> arr2 = new ArrayList<>();
        arr2.add(arr[0]);
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[i-1]) {
                arr2.add(arr[i]);
            }
        }
        for (int i : arr2) {
            System.out.print(i + " ");
        }

        // 2

//        System.out.print(arr[0] + " ");
//        for (int i = 1; i < arr.length; i++) {
//            if (arr[i] > arr[i-1]) {
//                System.out.print(arr[i] + " ");
//            }
//        }
    }
}
