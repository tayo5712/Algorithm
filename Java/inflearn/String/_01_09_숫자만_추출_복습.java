package String;

import java.util.*;

public class _01_09_숫자만_추출_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String ans = "";
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                ans += c;
            }
        }
        System.out.println(Integer.parseInt(ans));
    }
}
