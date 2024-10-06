package String;

import java.io.*;

public class _01_02_대소문자_변환_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] cc = br.readLine().toCharArray();
        for (char c : cc) {
            if (Character.isUpperCase(c)) {
                System.out.print(Character.toLowerCase(c));
            } else {
                System.out.print(Character.toUpperCase(c));
            }
        }
    }
}
