package 탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class _11724_연결요소의개수 {
    static ArrayList<Integer>[] arr;
    static boolean[] visited;
    static int result = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        arr = new ArrayList[N + 1];
        for (int i = 1; i < N + 1; i++) {       // 인접리스트 초기화
            arr[i] = new ArrayList<Integer>();
        }
         for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
             int u = Integer.parseInt(st.nextToken());
             int v = Integer.parseInt(st.nextToken());
             arr[u].add(v);     // 양방향
             arr[v].add(u);
        }
        visited = new boolean[N + 1];
        for (int i = 1; i < N + 1; i++) {
            if (!visited[i]) {  // 방문하지 않은 노드가 없을 때까지 반복
                result++;
                dfs(i);
            }

        }
        System.out.println(result);
    }
    static void dfs(int st) {
        if (visited[st]) {
            return;
        }
        visited[st] = true;
        for (int i : arr[st]) {
            if (visited[i] == false) {      // 연결 노드 중 방문하지 않았던 노드만 탐색
                dfs(i);
            }
        }
    }
}
