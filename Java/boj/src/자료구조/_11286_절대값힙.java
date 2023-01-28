package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class _11286_절대값힙 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> MyQueue = new PriorityQueue<>((o1, o2) -> {
            int a = Math.abs(o1);
            int b = Math.abs(o2);
            // 리턴 값이 음수면 o1 우선, 양수면 o2 우선
            if (a == b) {   // 1. 절대값이 같은 경우 음수 우선
                return o1 > o2 ? 1 : -1;
            } else {
                // 2. 절대값 작은 데이터 우선
                return a - b;
            }
        });
        for (int i = 0; i < N; i++) {
            int request = Integer.parseInt(br.readLine());
            if (request == 0) {
                if (MyQueue.isEmpty()) {
                    System.out.println(0);
                } else {
                    System.out.println(MyQueue.poll());
                }
            } else {
                MyQueue.add(request);
            }
        }
    }
}
