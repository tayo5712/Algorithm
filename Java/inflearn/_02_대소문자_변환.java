import java.util.Scanner;

public class _02_대소문자_변환 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        char[] cl = word.toCharArray();
        String result ="";
        for (char c : cl) {
            if (c >= 65 && c < 91) {
                result += Character.toLowerCase(c);
            } else {
                result += Character.toUpperCase(c);
            }
//            if (Character.isLowerCase(c)) {
//                result += Character.toUpperCase(c);
//            } else {
//                result += Character.toLowerCase(c);
//            }
        }
        System.out.println(result);
    }
}
