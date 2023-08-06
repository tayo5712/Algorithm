package 자료구조;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class _2163_카드게임 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Queue<Integer> myQueue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            myQueue.add(i); // 순서대로 큐에 카드 넣기
        }
        while (myQueue.size() > 1) {    // 한장 남을 때 까지
            myQueue.poll(); // 현재 가장 위의 카드 버리기
            myQueue.add(myQueue.poll());    // 현재 가장 위의 카드를 뺴서 아래로 넣기
        }
        System.out.println(myQueue.poll()); // 마지막 남은 한장 출력
    }
}
