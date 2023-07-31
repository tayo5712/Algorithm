package Greedy;

import java.util.*;

public class _09_04_최대수입스케쥴_PriorityQueue {
    static int max = 0;
    static class lecture implements Comparable<lecture> {
        int d;
        int m;
        public lecture(int d, int m) {
            this.d = d;
            this.m = m;
        }

        @Override
        public int compareTo(lecture o) {
            return o.m - this.m;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        int n  = sc.nextInt();
        ArrayList<lecture> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int d = sc.nextInt();
            int m = sc.nextInt();
            arr.add(new lecture(d, m));
            max = Math.max(max, d);
        }
        Collections.sort(arr);
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int j = 0;
        for (int i = max; i >= 1; i--) {
            for (; j < n; j++) {
                if (arr.get(j).m < i) break;
                pq.offer(arr.get(j).d);
            }
            if (!pq.isEmpty()) answer += pq.poll();
        }
        System.out.println(answer);
    }
}
