package String;

import java.util.Scanner;

public class _01_12_암호_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        String s = sc.next();
        s = s.replace('#', '1').replace('*', '0');
        String answer = "";
        for (int i = 0; i < n; i++) {
            String code = s.substring(0, 7);
            s = s.substring(7);
            answer += (char) Integer.parseInt(code, 2);
        }
        System.out.println(answer);
    }
}
