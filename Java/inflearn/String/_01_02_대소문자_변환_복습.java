package String;

import java.util.Scanner;

public class _01_02_대소문자_변환_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        String new_word = "";
        for (char c : word.toCharArray()) {
            if (Character.isUpperCase(c)) {
                new_word += Character.toLowerCase(c);
            } else {
                new_word += Character.toUpperCase(c);
            }
        }
        System.out.println(new_word);
    }
}
