package Array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class _02_02_보이는학생_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int cnt = 1;
        int tall = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > tall) {
                tall = arr[i];
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
