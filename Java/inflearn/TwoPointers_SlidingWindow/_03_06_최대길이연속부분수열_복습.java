package TwoPointers_SlidingWindow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _03_06_최대길이연속부분수열_복습 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int lt = 0;
        int answer = 0;
        int len = 0;
        for (int rt = 0; rt < n; rt++) {
            if (arr[rt] == 1) {
                len++;
            }
            else {
                if (k > 0) {
                    k--;
                    len++;
                }
                else {
                    while (arr[lt] != 0) {
                        lt++;
                        len--;
                    }
                    lt++;
                }
            }
            answer = Math.max(answer, len);
        }
        System.out.println(answer);
    }
}
