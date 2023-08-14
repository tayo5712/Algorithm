import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _모의역량_요리사 {
    static int n = 0;
    static int answer;
    static int[] visited;
    static int[][] ingredient;
    static void cook(int depth, int st) {
        if (depth == n/2) { // 절반 확인
            ArrayList<Integer> a = new ArrayList<>();
            ArrayList<Integer> b = new ArrayList<>();
            for (int i = 1; i <= n; i++) {
                if (visited[i] == 1) a.add(i);
                else b.add(i);
            }
            int aFlavor = 0;
            int bFlavor = 0;
            for (int i = 0; i < a.size(); i++) {
                for (int j = i+1; j < a.size(); j++) {
                    aFlavor += ingredient[a.get(i)-1][a.get(j)-1] + ingredient[a.get(j)-1][a.get(i)-1];
                }
            }
            for (int i = 0; i < b.size(); i++) {
                for (int j = i+1; j < b.size(); j++) {
                    bFlavor += ingredient[b.get(i)-1][b.get(j)-1] + ingredient[b.get(j)-1][b.get(i)-1];
                }
            }
            answer = Math.min(answer, Math.abs(aFlavor - bFlavor));
        }
        else {
            for (int i = st; i < n; i++) {
                visited[i] = 1;
                cook(depth + 1, i + 1);
                visited[i] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            answer = Integer.MAX_VALUE;
            n = Integer.parseInt(br.readLine());
            ingredient = new int[n][n];
            visited = new int[n+1];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    ingredient[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            cook(0, 1);
            System.out.println("#" + tc + " " + answer);
        }
    }
}