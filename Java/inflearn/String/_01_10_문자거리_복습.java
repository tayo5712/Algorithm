package String;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class _01_10_문자거리_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        int n = s.length();
        char[] cc = s.toCharArray();
        char target = st.nextToken().charAt(0);
        int[] distance = new int[n];
        int pos = 101;
        for (int i = 0; i < n; i++) {
            if (cc[i] == target) {
                distance[i] = 0;
                pos = i;
            } else {
                distance[i] = Math.abs(pos - i);
            }
        }
        pos = 101;
        for (int i = n - 1; i >= 0; i--) {
            if (cc[i] == target) {
                pos = i;
            } else {
                distance[i] = Math.min(distance[i], pos - i);
            }
        }
        for (int i : distance) {
            System.out.print(i + " ");
        }
    }
}
