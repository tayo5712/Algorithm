package String;

import java.util.Scanner;

public class _01_07_회문문자열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word1 = sc.next();
        StringBuilder sd = new StringBuilder(word1);
        String word2 = String.valueOf(sd.reverse());
        if (word1.equalsIgnoreCase(word2)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
