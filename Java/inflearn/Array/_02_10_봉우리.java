package Array;

import java.util.Scanner;

public class _02_10_봉우리 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        int result = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                boolean flag = true;
                for (int k = 0; k < 4; k++) {
                    int nr = i + dr[k];
                    int nc = j + dc[k];
                    if (nr >= 0 && nr < n && nc >=0 && nc < n && arr[nr][nc] >= arr[i][j]) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    result++;
                }
            }
        }
        System.out.println(result);

//        int[][] arr = new int[n + 2][n + 2];
//        for (int i = 0; i < n + 2; i++) {
//            for (int j = 0; j < n + 2; j++) {
//                if (i == 0 || i == n+1 || j == 0 || j == n+1) {
//                    arr[i][j] = 0;
//                }
//                else {
//                    arr[i][j] = sc.nextInt();
//                }
//            }
//        }
//
//        int peek = 0;
//        for (int i = 1; i < n+1; i++) {
//            for (int j = 1; j < n+1; j++) {
//                if (arr[i][j] > arr[i - 1][j] && arr[i][j] > arr[i][j - 1] && arr[i][j] > arr[i][j + 1] && arr[i][j] > arr[i + 1][j]) {
//                    peek++;
//                }
//            }
//        }
//        System.out.println(peek);
    }
}
