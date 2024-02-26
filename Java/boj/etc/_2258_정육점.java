package etc;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] meats = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int weight = Integer.parseInt(st.nextToken());
            int price = Integer.parseInt(st.nextToken());
            meats[i][0] = weight;
            meats[i][1] = price;
        }
        Arrays.sort(meats, new Comparator<int[]>() {
            @Override
            public int compare(int[]o1, int[]o2) {
                if (o1[1] == o2[1]) {
                    return o2[0] - o1[0];
                }
                return o1[1] - o2[1];
            }
        });
        int sumW = 0, same = 0;
        long answer = 2147483648L;
        for (int i = 0; i < n; i++) {
            sumW += meats[i][0];
            if (i >= 1 && meats[i - 1][1] == meats[i][1]) {
                same += meats[i][1];
            }
            else {
                same = 0;
            }
            if (sumW >= m) {
                answer = Math.min(answer, meats[i][1] + same);
            }
        }
        if (answer == 2147483648L) {
            System.out.println(-1);
        }
        else {
            System.out.println(answer);
        }
    }
}
