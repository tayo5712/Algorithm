package String;

import java.util.Scanner;

public class _01_03_문장_속_단어_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] words = sc.nextLine().split(" ");
        String result = "";
        for (String s : words) {
            if (result.length() < s.length()) {
                result = s;
            }
        }
        System.out.println(result);
    }
}
