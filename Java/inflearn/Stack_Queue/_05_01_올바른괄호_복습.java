package Stack_Queue;

import java.util.Scanner;
import java.util.Stack;

public class _05_01_올바른괄호_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] arr = sc.next().toCharArray();
        Stack<Character> st = new Stack<>();
        boolean flag = true;
        for (char c : arr) {
            if (c == '(') st.push(c);
            else {
                if (st.isEmpty() || st.pop() != '(') {
                    flag = false;
                    break;
                }
            }
        }
        if (!st.isEmpty()) flag = false;
        if (flag) System.out.println("YES");
        else System.out.println("NO");
    }
}
