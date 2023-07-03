package String;

import java.util.Scanner;

public class _01_04_단어_뒤집기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String word = sc.next();
            // 1
//            StringBuilder sb = new StringBuilder(word);
            // String result = new StringBuilder(word).reverse().toString();
//            System.out.println(sb.reverse());

            // 2
            char[] cl = word.toCharArray();
            for (int j = 0; j < cl.length/2; j++) {
                int pos = cl.length - (j + 1);
                char tmp = cl[pos];
                cl[pos] = cl[j];
                cl[j] = tmp;
            }
            String s = String.valueOf(cl);
            System.out.println(s);
        }
    }
}
