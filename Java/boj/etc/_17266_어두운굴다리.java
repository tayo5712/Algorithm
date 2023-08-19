package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _17266_어두운굴다리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] lamp = new int[m];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            lamp[i] = Integer.parseInt(st.nextToken());
        }
        int area = Math.max(lamp[0], n-lamp[m-1]);
        for (int i = 1; i < m; i++) {
            int range = (int) Math.ceil((lamp[i] - lamp[i-1]) / 2.0);
            area = Math.max(area, range);
        }
        System.out.println(area);
    }
}
