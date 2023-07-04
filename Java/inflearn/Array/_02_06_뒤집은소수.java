package Array;

import java.util.ArrayList;
import java.util.Scanner;

public class _02_06_뒤집은소수 {
    public static boolean isPrime(int num) {
        if (num == 1) return false;
        for(int i=2; i<num; i++) {
            if(num%i==0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        // 1
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int tmp = arr[i];
            int res = 0;
            while (tmp > 0) {
                int t = tmp%10;
                res = res * 10 + t;
                tmp = tmp/10;
            }
            if (isPrime(res)) {
                answer.add(res);
            }
//            int tmp = Integer.parseInt(String.valueOf(new StringBuilder(arr[i]).reverse()));
        }
        for (int i : answer) {
            System.out.print(i + " ");
        }


        // 2
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[] arr = new int[100000];
//        arr[1] = 1;
//        for (int i = 2; i <= 99999 ; i++) {
//            if (arr[i] == 0) {
//                for (int j = i ; j <= 99999; j += i) {
//                    if (j != i) {
//                        arr[j] = 1;
//                    }
//                }
//            }
//        }
//        for (int i = 0; i < n; i++) {
//            int index = Integer.parseInt(String.valueOf(new StringBuilder(sc.next()).reverse()));
//            if (arr[index] == 0) {
//                System.out.print(index + " ");
//            }
//        }
    }
}
