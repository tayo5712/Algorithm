package String;

import java.util.Scanner;

public class _01_08_유효한_팰린드롬_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word1 = sc.nextLine().replaceAll("[^a-zA-Z]", "");
        String word2 = new StringBuilder(word1).reverse().toString();
        if (word1.equalsIgnoreCase(word2)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
