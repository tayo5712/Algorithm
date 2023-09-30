package String;

import java.util.Scanner;

public class _01_08_유효한_팰린드롬_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        word = word.replaceAll("[^a-zA-Z]", "");
        if (word.equalsIgnoreCase(new StringBuilder(word).reverse().toString())) System.out.println("YES");
        else System.out.println("NO");
    }
}
