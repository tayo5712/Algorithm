package 자료구조;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class _1874_스택수열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        boolean flag = true;
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        Stack<Integer> stack = new Stack<>();
        List<String> result = new ArrayList<>();
        int num = 1;    // 오름차순 수
        for (int i = 0; i < N ; i++) {
            if (arr[i] >= num) {
                while (arr[i] >= num) { // 현재 수열 값 >= 오름차순 자연수: 갑싱 같아질 떄까지 push()한 후 pop()
                    stack.push(num++);
                    result.add("+");
                }
                stack.pop();
                result.add("-");
            } else {    // 현재 수열 값 < 오름차순 자연수 이면 pop()을 수행해 수열 원소를 꺼냄
                int n = stack.pop();
                if (n > arr[i]) {   // 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열 출력불가
                    System.out.println("NO");
                    flag = false;
                    break;
                } else {
                    result.add("-");
                }
            }
        }
        if (flag) {
            for ( String oper : result) {
                System.out.println(oper);
            }
        }
    }
}
