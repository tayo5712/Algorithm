package String;

import java.util.Scanner;

public class _01_06_중복문자제거 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String words = sc.next();
        String result = "";
        for (int i = 0; i < words.length(); i++) {
            if (i == words.indexOf(words.charAt(i))) {
                result += words.charAt(i);
            }
        }
        System.out.println(result);

    }
}
