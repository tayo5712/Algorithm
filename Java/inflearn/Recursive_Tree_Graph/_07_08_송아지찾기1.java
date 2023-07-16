package Recursive_Tree_Graph;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Position {
    int position;
    int cnt;

    public Position(int now, int cnt) {
        position = now;
        this.cnt = cnt;
    }
}

public class _07_08_송아지찾기1 {
    Position pos;

    public void BFS(Position pos, int e) {
        Queue<Position> myQueue = new LinkedList<>();
        myQueue.offer(pos);
        int[] np = {-1, 1, 5};
        int[] visited = new int[10001];
        visited[pos.position] = 1;
        while (!myQueue.isEmpty()) {
            Position nowP = myQueue.poll();
            if (nowP.position == e) {
                System.out.println(nowP.cnt);
                break;
            }
            for (int i = 0; i < 3; i++) {
                int nextPosition = nowP.position + np[i];
                if (nextPosition <= 0 || nextPosition > 10000 || visited[nextPosition] == 1) continue;
                visited[nextPosition] = 1;
                Position next = new Position(nextPosition, nowP.cnt + 1);
                myQueue.offer(next);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int e = sc.nextInt();

        _07_08_송아지찾기1 m = new _07_08_송아지찾기1();
        m.pos = new Position(s, 0);
        m.BFS(m.pos, e);

    }
}
