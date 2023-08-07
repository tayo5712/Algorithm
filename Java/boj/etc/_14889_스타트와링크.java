package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _14889_스타트와링크 {
    static int n;
    static int answer = Integer.MAX_VALUE;
    static int[] visited;
    static int[][] arr;
    static void DFS(int L, int S) {
        if (L == n / 2) {
            ArrayList<Integer> start = new ArrayList<>();
            ArrayList<Integer> link = new ArrayList<>();
            for (int i = 1; i <= n; i++) {
                if (visited[i] == 1) start.add(i);
                else link.add(i);
            }
            int sp = 0, lp = 0;
            for (int i = 0; i < n/2; i++) {
                for (int j = i + 1; j < n/2 ; j++) {
                    sp += arr[start.get(i)][start.get(j)] + arr[start.get(j)][start.get(i)];
                    lp += arr[link.get(i)][link.get(j)] + arr[link.get(j)][link.get(i)];
                }
            }
            answer = Math.min(answer, Math.abs(sp-lp));
        }
        else {
            for (int i = S; i <= n; i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    DFS(L + 1, i + 1);
                    visited[i] = 0;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        arr = new int[n+1][n+1];
        visited = new int[n+1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        DFS(0, 1);
        // 순열 n 개중 n / 2 개 만큼 뽑기
        System.out.println(answer);
    }
}
