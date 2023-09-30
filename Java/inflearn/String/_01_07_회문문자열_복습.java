package String;

import java.util.Scanner;

public class _01_07_회문문자열_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        word = word.toUpperCase();
        if (word.equals(new StringBuilder(word).reverse().toString())) System.out.println("YES");
        else System.out.println("NO");
    }
}
