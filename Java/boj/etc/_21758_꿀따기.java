
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] honey = new int[n];
        for (int i = 0; i < n; i++) {
            honey[i] = Integer.parseInt(st.nextToken());
        }
        long[] sumV = new long[n];
        sumV[0] = honey[0];
        for (int i = 1; i < n; i++) {
            sumV[i] = sumV[i-1] + honey[i];
        }
        long ans = 0;

        // case1 : 꿀통이 맨 왼쪽 (벌1은 n-1위치 벌2는 i위치)
        for (int i = 1; i < n - 1; i++) {
            ans = Math.max(ans, sumV[n-2] + sumV[i - 1] - honey[i]);
        }
        // case2 : 꿀통이 맨 오른쪽 (벌1은 0위치 벌2는 i위치)
        for (int i = 1; i < n - 1; i++) {
            ans = Math.max(ans, sumV[n-1] - honey[0] - honey[i] + sumV[n-1] - sumV[i]);
        }
        // case3 : 꿀통이 가운데 (벌1은 0위치 벌2는 n-1위치, 꿀통은 i위치)
        for (int i = 1; i < n - 1; i++) {
            ans = Math.max(ans, sumV[i] - honey[0] + sumV[n-2] - sumV[i - 1]);
        }
        System.out.println(ans);

    }
}
