package Recursive_Tree_Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _07_11_그래프와인접행렬 {
    static int n, m, answer = 0;
    static int[][] arr;
    public void DFS(int v, int[] visited) {
        if (v == n) {
            answer++;
        } else {
            for (int i = 1; i < n + 1; i++) {
                if (arr[v][i] == 1 && visited[i] == 0) {
                    visited[i] = 1;
                    DFS(i, visited);
                    visited[i] = 0;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n+1][n+1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = 1;
        }
        int[] visited = new int[n + 1];
        visited[1] = 1;
        _07_11_그래프와인접행렬 T = new _07_11_그래프와인접행렬();
        T.DFS(1, visited);
        System.out.println(answer);

    }
}
