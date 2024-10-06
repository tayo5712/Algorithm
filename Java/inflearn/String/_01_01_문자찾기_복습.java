package String;

import java.util.Scanner;

public class _01_01_문자찾기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char c = sc.next().charAt(0);
        c = Character.toUpperCase(c);

        int result = 0;
        s = s.toUpperCase();
        for (char cc : s.toCharArray()) {
            if (cc == c) {
                result++;
            }
        }
        System.out.println(result);
    }
}
