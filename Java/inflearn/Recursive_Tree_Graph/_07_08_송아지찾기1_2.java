package Recursive_Tree_Graph;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class _07_08_송아지찾기1_2 {
    public int BFS(int s, int e) {
        int[] visited = new int[10001];
        int level = 0;
        int[] next = {-1, 1, 5};
        Queue<Integer> myQueue = new LinkedList<>();
        visited[s] = 1;
        myQueue.offer(s);
        while (!myQueue.isEmpty()) {
            int len = myQueue.size();
            for (int i = 0; i < len; i++) {
                int now = myQueue.poll();
                for (int j = 0; j < 3; j++) {
                    int nx = now + next[j];
                    if (nx == e) return level+1;
                    if (nx > 0 && nx <= 10000 && visited[nx] == 0) {
                        visited[nx] = 1;
                        myQueue.offer(nx);
                    }
                }
            }
            level++;
        }
        return 0;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int e = sc.nextInt();

        _07_08_송아지찾기1_2 problem = new _07_08_송아지찾기1_2();
        System.out.println(problem.BFS(s, e));
    }
}
