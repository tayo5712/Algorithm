package 자료구조;

import java.io.*;
import java.util.*;

public class _11003_최솟값찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        LinkedList<Node> arr = new LinkedList<>();  // 데이터 추가, 삭제가 잦기 때문에 LinkedList 이용
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(st.nextToken());
            while (!arr.isEmpty() && arr.getLast().value > a) { // 리스트에 들어있는 값이 현재 값보다 크면 필요 없으므로 삭제
                arr.removeLast();
            }
            arr.add(new Node(a, i));    // 현재 값 추가
            if (arr.getFirst().index <= i - L) {    // L 범위 넘은 값은 삭제
                arr.removeFirst();
            }
            bw.write(arr.getFirst().value + " ");
        }
        bw.flush();
        bw.close();
    }

    static class Node {
        public int value;
        public int index;

        public Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}
