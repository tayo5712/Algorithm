package String;

import java.util.Scanner;

public class _01_04_단어_뒤집기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.next());
        for (int i = 0; i < T; i++) {
            String word = sc.next();
            StringBuilder sb = new StringBuilder(word);
            String result = String.valueOf(sb.reverse());
            System.out.println(result);
        }
    }
}
