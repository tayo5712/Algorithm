package String;

import java.util.Scanner;

public class _01_04_단어_뒤집기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            StringBuilder sb = new StringBuilder(s);
            System.out.println(sb.reverse());
        }
    }
}
