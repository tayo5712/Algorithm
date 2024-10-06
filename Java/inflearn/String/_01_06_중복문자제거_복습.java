package String;

import java.util.Scanner;

public class _01_06_중복문자제거_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        String ans = "";
        for (int i = 0; i < word.length(); i++) {
            if (i == word.indexOf(word.charAt(i))) {
                ans += word.charAt(i);
            }
        }
        System.out.println(ans);
    }
}
