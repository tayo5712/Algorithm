package Array;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class _02_11_임시반장정하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n+1][6];
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < 6; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        int max=0, index=0;
        for (int i = 1; i < n+1; i++) {
            int cnt = 0;
            for (int j = 0; j < n + 1; j++) {
                for (int k = 1; k < 6; k++) {
                    if (arr[i][k] == arr[j][k]) {
                        cnt++;
                        break;
                    }
                }
            }
            if (cnt > max) {
                max = cnt;
                index = i;
            }
        }

        System.out.println(index);
    }
}
