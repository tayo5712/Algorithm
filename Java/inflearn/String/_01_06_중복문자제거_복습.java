package String;

import java.util.Scanner;

public class _01_06_중복문자제거_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        String answer = "";
        for (int i = 0; i < word.length(); i++) {
            char w = word.charAt(i);
            if (word.indexOf(w) == i) answer += w;
        }
        System.out.println(answer);
    }
}
