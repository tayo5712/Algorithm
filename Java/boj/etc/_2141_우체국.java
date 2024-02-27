
package etc;
import java.util.*;
import java.io.*;

public class _2141_우체국 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int[][] arr = new int[n][2];
        long totalNum = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
            totalNum += arr[i][1];
        }
        Arrays.sort(arr, (o1, o2) -> o1[0] - o2[0]);
        long nowNum = 0;
        for (int i = 0; i < n; i++) {
            nowNum += arr[i][1];
            if (nowNum >= (totalNum + 1) / 2) {
                System.out.println(arr[i][0]);
                break;
            }
        }
    }
}
