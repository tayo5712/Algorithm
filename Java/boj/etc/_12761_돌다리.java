package DFS_BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class TEST {
    static class DongGu {
        int pos;
        int cnt;
        public DongGu(int pos, int cnt) {
            this.pos = pos;
            this.cnt = cnt;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] dr = {1, -1, A, B, -A, -B};
        Queue<DongGu> q = new LinkedList<>();
        int[] visited = new int[100001];
        visited[N] = 1;
        q.offer(new DongGu(N, 0));
        while (!q.isEmpty()) {
            DongGu now = q.poll();
            if (now.pos == M) {
                System.out.println(now.cnt);
                break;
            }
            for (int i = 0; i<6; i++) {
                int ni = now.pos + dr[i];
                if (ni >= 0 && ni <= 100000 && visited[ni] == 0) {
                    visited[ni] = 1;
                    q.offer(new DongGu(ni, now.cnt + 1));
                }
                if (i == 2 || i == 3) {
                    ni = now.pos * dr[i];
                    if (ni >= 0 && ni <= 100000 && visited[ni] == 0) {
                        visited[ni] = 1;
                        q.offer(new DongGu(ni, now.cnt + 1));
                    }
                }
            }
        }
    }
}
