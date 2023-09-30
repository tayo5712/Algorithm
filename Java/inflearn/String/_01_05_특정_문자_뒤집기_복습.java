package String;

import java.util.*;
public class _01_05_특정_문자_뒤집기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        int st = 0;
        int ed = word.length()-1;
        char[] cr = word.toCharArray();
        while (st < ed) {
            if (!Character.isAlphabetic(cr[st])) {
                st++;
            } else if (!Character.isAlphabetic(cr[ed])) {
                ed--;
            } else {
                char tmp = cr[st];
                cr[st] = cr[ed];
                cr[ed] = tmp;
                st++;
                ed--;
            }
        }
        System.out.println(String.valueOf(cr));
    }
}
