package String;

import java.util.Scanner;

public class _01_09_숫자만_추출 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        String result = "";
        for (char c : word.toCharArray()) {
            // 1
            if (c >= 48 && c <= 57) {
                result += c;
            }
            // 2
//            if (Character.isDigit(c)) {
//                result += c;
//            }
        }
        System.out.println(Integer.parseInt(result));
    }
}
