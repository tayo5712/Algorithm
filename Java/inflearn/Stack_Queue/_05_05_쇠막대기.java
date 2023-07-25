package Stack_Queue;

import java.util.Scanner;
import java.util.Stack;

public class _05_05_쇠막대기 {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        String s = sc.next();
//        char[] arr = s.toCharArray();
//        Stack<Character> bar = new Stack<>();
//        bar.push('(');
//        int answer = 0;
//        for (int i = 1; i < arr.length; i++) {
//            if (arr[i] == '(') {
//                bar.push('(');
//            }
//            else {
//                if (arr[i-1] == '(') {
//                    bar.pop();
//                    answer += bar.size();
//                } else {
//                    bar.pop();
//                    answer += 1;
//                }
//            }
//        }
//        System.out.println(answer);
//    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char[] arr = s.toCharArray();
        int bar = 1;
        int answer = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == '(') {
                bar += 1;
            }
            else {
                bar -= 1;
                if (arr[i-1] == '(') {
                    answer += bar;
                } else {
                    answer += 1;
                }
            }
        }
        System.out.println(answer);
    }
}
