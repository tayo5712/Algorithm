import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int minV = b;
        for (int i = 0; i < h; i++) {
            int pee = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                int possible = Integer.parseInt(st.nextToken());
                if (possible >= n) {
                    minV = Math.min(minV, n * pee);
                }
            }
        }
        if (minV == b) {
            System.out.println("stay home");
        } else {
            System.out.println(minV);
        }
    }
}
