package etc;

import java.util.Scanner;

public class _19532_수학은비대면강의입니다 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = sc.nextInt();
        int f = sc.nextInt();
        boolean flag = true;
        for (int x = -999; x <= 999; x++) {
            if (!flag) break;
            for (int y = -999; y <= 999; y++) {
                if (a * x + b * y == c && d * x + e * y == f) {
                    flag = false;
                    System.out.println(x + " " + y);
                    break;
                }
            }
        }
    }
}
