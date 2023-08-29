import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1486_장훈이의높은선반 {
    static int N, B = 0;
    static int answer = 0;
    static int[] heights;
    static void stack(int depth, int sum) {
        if (sum >= B && sum < answer) {
            answer = sum;
        }
        if (depth == N) return;
        else {
            stack(depth+1, sum + heights[depth]);
            stack(depth+1,  sum);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            heights = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                heights[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(heights);
            answer = Integer.MAX_VALUE;
            stack(0, 0);
            System.out.println("#" + tc + " " + (answer-B));
        }
    }
}
