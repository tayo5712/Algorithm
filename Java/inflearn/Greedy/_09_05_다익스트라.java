package Greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class _09_05_다익스트라 {
    static class Node implements Comparable<Node> {
        public int node;
        public int weight;
        public Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }
        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
        for (int i = 0; i <= n ; i++) {
            graph.add(new ArrayList<Node>());
        }
        int[][] arr = new int[n+1][n+1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, c));
        }
        int[] value = new int[n+1];
        Arrays.fill(value, Integer.MAX_VALUE);
        value[1] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(1, 0));
        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (now.weight > value[now.node]) continue;
            for (Node nowNode : graph.get(now.node)) {
                if (value[nowNode.node] > now.weight + nowNode.weight)
                    value[nowNode.node] = now.weight+nowNode.weight;
                    pq.offer(new Node(nowNode.node, now.weight+nowNode.weight));
            }
        }
        for (int i = 2; i <= n; i++) {
            if (value[i] != Integer.MAX_VALUE) System.out.println(i + " : " + value[i]);
            else System.out.println(i + " : impossible");
        }
    }
}
