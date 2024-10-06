package String;

import java.util.Scanner;

public class _01_07_회문문자열_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.next();
        String s2 = new StringBuilder(s1).reverse().toString();
        if (s1.equalsIgnoreCase(s2)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
