package Stack_Queue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class _05_06_공주구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            q.offer(i);
        }
        int num = 0;
        while (q.size() != 1) {
            int prince = q.poll();
            if (++num != k) q.offer(prince);
            else num = 0;
        }
        System.out.println(q.poll());
    }
}
