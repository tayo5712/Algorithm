package Stack_Queue;

import java.util.Scanner;
import java.util.Stack;

public class _05_01_올바른괄호 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Stack<Character> st = new Stack<>();
        Boolean answer = true;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                st.push(c);
            } else if (c == ')') {
                if (!st.isEmpty() && st.peek() == '(')
                    st.pop();
                else {
                    answer = false;
                    break;
                }
            }
        }
        if (answer && st.size() == 0) System.out.println("YES");
        else System.out.println("NO");
    }
}
