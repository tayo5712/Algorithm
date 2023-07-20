package Recursive_Tree_Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _07_14_그래프최단거리 {
    static int n, m, answer = 0;
    static ArrayList<ArrayList<Integer>> graph;

    public void BFS(int v) {
        int L = 0;
        int[] result = new int[n + 1];
        int[] visited = new int[n + 1];
        visited[1] = 1;
        Queue<Integer> Q = new LinkedList<>();
        Q.offer(v);
        while (!Q.isEmpty()) {
            int len = Q.size();
            for (int j = 0; j < len; j++) {
                int i = Q.poll();
                if (result[i] == 0) result[i] = L;
                for (int d : graph.get(i)) {
                    if (visited[d] == 0) {
                        visited[d] = 1;
                        Q.offer(d);
                    }
                }
            }
            L++;
        }
        for (int i = 2; i < n + 1; i++) {
            System.out.println(i + " : " + result[i]);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        graph = new ArrayList<ArrayList<Integer>>();
        m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
        }
        _07_14_그래프최단거리 T = new _07_14_그래프최단거리();
        T.BFS(1);
    }
}
