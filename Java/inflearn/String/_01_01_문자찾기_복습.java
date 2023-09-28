package String;

import java.util.Scanner;

public class _01_01_문자찾기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char a = sc.next().charAt(0);

        str = str.toUpperCase();
        a = Character.toUpperCase(a);
        int cnt = 0;

        for (char c : str.toCharArray()) {
            if (c == a) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
