package String;

import java.util.Scanner;

public class _01_03_문장_속_단어_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String[] arr = s.split(" ");
        String maxWord = "";
        for (String str : arr) {
            if (str.length() > maxWord.length()) {
                maxWord = str;
            }
        }
        System.out.println(maxWord);
    }
}
