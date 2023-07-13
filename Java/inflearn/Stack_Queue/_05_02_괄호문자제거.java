package Stack_Queue;

import java.util.Scanner;
import java.util.Stack;

public class _05_02_괄호문자제거 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Stack<Character> st = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c != ')') {
                st.push(c);
            }
            else {
                while (!st.isEmpty() && st.pop() != '(');
            }
        }
        for (char c : st) {
            System.out.print(c);
        }
    }
}
