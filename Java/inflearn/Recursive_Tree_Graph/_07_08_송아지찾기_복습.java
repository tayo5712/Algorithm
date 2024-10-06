package Recursive_Tree_Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _07_08_송아지찾기_복습 {
    static class cow {
        int pos;
        int jump;

        public cow(int pos, int jump) {
            this.pos = pos;
            this.jump = jump;
        }
    }
    static int bfs(int s, int e) {
        Queue<cow> q = new LinkedList<>();
        int[] np = {-1, 1, 5};
        int[] visited = new int[10001];
        q.offer(new cow(s, 0));
        while (!q.isEmpty()) {
            cow tmp = q.poll();
            for (int i = 0; i < 3; i++) {
                int nextP = tmp.pos + np[i];
                if (nextP == e) return tmp.jump + 1;
                if (nextP > 0 && nextP <= 10000 && visited[nextP] == 0) {
                    visited[nextP] = 1;
                    q.offer(new cow(nextP, tmp.jump + 1));
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        System.out.println(bfs(s, e));
    }
}
