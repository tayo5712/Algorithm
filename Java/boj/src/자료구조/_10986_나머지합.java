package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10986_나머지합 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 결과 값 담을 변수
        long result = 0;

        // 합배열 만들기
        long[] sumArr = new long[N + 1];
        // 나머지 배열
        long[] remains = new long[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            long A = Integer.parseInt(st.nextToken());
            sumArr[i] = sumArr[i - 1] + A;
            long remain = sumArr[i] % M;
            if (remain == 0) {
                result += 1;
            }
            remains[(int) remain] += 1;
        }
        for (int i = 0; i < M; i++) {
            if (remains[i] > 1) {
                result += (remains[i] * (remains[i]-1)) / 2;
            }
        }
        System.out.println(result);
    }
}
