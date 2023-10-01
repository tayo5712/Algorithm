package String;

import java.util.Scanner;

public class _01_11_문자열압축_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        str += " ";
        String answer = "";
        int pos = 1;
        for (int i = 0; i < str.length()-1; i++) {
            if (str.charAt(i) == str.charAt(i + 1)) {
                pos++;
            } else {
                answer += str.charAt(i);
                if (pos > 1) {
                    answer += pos;
                }
                pos = 1;
            }
        }
        System.out.println(answer);
    }
}
