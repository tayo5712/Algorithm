package String;

import java.util.Scanner;

public class _01_11_문자열압축_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next() + " ";
        char before = s.charAt(0);
        int count = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == before) {
                count++;
            } else {
                System.out.print(before);
                if (count > 1) {
                    System.out.print(count);
                }
                before = s.charAt(i);
                count = 1;
            }
        }
    }
}
