package 자료구조;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class _17298_오큰수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> myStack = new Stack<>();
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] result = new int[N];  // 정답 배열
        int[] arr = new int[N]; // 수열 배열
        myStack.push(0);    // 처음에 스택 비어있으므로 시작 인덱스 0 으로 초기화
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 1; i < N; i++) {
            while (!myStack.isEmpty() && arr[myStack.peek()] < arr[i]) {    // 스택이 비어있지 않고 현재 수열이 스택의 top 인덱스가 가리키는 수열보다 클 경우
                result[myStack.pop()] = arr[i]; // 정답 배열에 오큰수를 현재 수열로 저장
            };
            myStack.push(i);    // 인덱스 추가
        }
        while (!myStack.isEmpty()) {    // 반복문을 다 돌고 나왔는데도 스택이 비어있지 않으면
            result[myStack.pop()] = -1; // 해당 인덱스에 -1 넣어주기
        }
        for (int i = 0; i < N; i++) {
            bw.write(result[i] + " ");
        }
        bw.flush();
        bw.close();
    }
}
