package String;

import java.util.Scanner;

public class _01_12_암호_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        String ans = "";
        s = s.replace('#', '1').replace('*', '0');
        for (int i = 0; i < n; i++) {
            String code = s.substring(0, 7);
            s = s.substring(7);
            int decimal = Integer.parseInt(code, 2);
            ans += (char) decimal;
        }
        System.out.println(ans);
    }
}
