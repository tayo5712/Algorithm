package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _12847_꿀아르바이트 {

    static int n,m;
    static long max;
    static int[] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            map[i] = Integer.parseInt(st.nextToken());
        }

        long sum = 0;

        // 크기가 m 인 윈도우가 이동한다고 생각하면 쉬울 듯
        // 따라서 현재 윈도우의 가장 첫번째 원소의 값을 빼고
        // 앞으로 추가될 다음 원소의 값을 윈도우에 더하여
        // 윈도우의 값을 얻을 수 있다.

        for (int i = 0; i < m; i++) {
            sum += map[i];
        }

        max = sum;

        for (int i = m; i < n; i++) {
            sum += (map[i] - map[i-m]);
            max = Math.max(max, sum);
        }
        System.out.println(max);

    }
}
