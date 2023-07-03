package Array;

import java.util.Scanner;

public class _02_03_가위바위보 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[2][n];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < n; i++) {
            int A = arr[0][i];
            int B = arr[1][i];
            if (A == B) {
                System.out.println('D');
            }
            else if (A == 1) {
                if (B == 2) System.out.println('B');
                else System.out.println('A');
            }
            else if (A == 2) {
                if (B == 1) System.out.println('A');
                else System.out.println('B');
            }
            else {
                if (B == 1) System.out.println('B');
                else System.out.println('A');
            }
        }
    }
}
