package DynamicProgramming_동적계획법;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class _10_04_가장높은탑쌓기 {
    static class brick implements Comparable<brick> {
        int width;
        int height;
        int weight;
        public brick(int width, int height, int weight) {
            this.width = width;
            this.height = height;
            this.weight = weight;
        }

        @Override
        public int compareTo(brick o) {
            return o.width - this.width;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        ArrayList<brick> bricks = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int width = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            bricks.add(new brick(width, height, weight));
        }
        Collections.sort(bricks);
        int[] dp = new int[n];
        int answer = 0;
        dp[0] = bricks.get(0).height;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (bricks.get(i).weight < bricks.get(j).weight) dp[i] = Math.max(dp[i], dp[j]);
            }
            dp[i] += bricks.get(i).height;
            answer = Math.max(answer, dp[i]);
        }
        System.out.println(answer);
    }
}
