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
        int result = 0;

        // 합배열 만들기
        long[] sumArr = new long[N + 1];
        // 나머지 배열
        int[] remains = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            int A = Integer.parseInt(st.nextToken());
            sumArr[i] = sumArr[i - 1] + A;
            int remain = (int) (sumArr[i] % M);
            if (remain == 0) {
                result += 1;
            }
            remains[remain] += 1;
        }
        for (int i = 1; i < M; i++) {
            result += (remains[i] * (remains[i]-1)) / 2;
        }
        System.out.println(result);
    }
}
