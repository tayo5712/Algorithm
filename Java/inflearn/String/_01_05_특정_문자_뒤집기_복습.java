package String;

import java.util.*;
public class _01_05_특정_문자_뒤집기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] cc = sc.next().toCharArray();
        int l = 0;
        int r = cc.length - 1;
        while (l < r) {
            if (!Character.isAlphabetic(cc[l])) {
                l++;
            }
            else if (!Character.isAlphabetic(cc[r])) {
                r--;
            }
            else if (Character.isAlphabetic(cc[l]) && Character.isAlphabetic(cc[r])) {
                char tmp = cc[r];
                cc[r] = cc[l];
                cc[l] = tmp;
                l++;
                r--;
            }
        }
        System.out.println(String.valueOf(cc));
    }
}
