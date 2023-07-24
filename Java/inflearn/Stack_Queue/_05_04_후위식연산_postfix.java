package Stack_Queue;

import java.util.Scanner;
import java.util.Stack;

public class _05_04_후위식연산_postfix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        String s = sc.next();
        Stack<Integer> st = new Stack<>();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) st.push(Character.getNumericValue(c));
            else {
                int rt = st.pop();
                int lt = st.pop();
                if (c == '+') st.push(lt + rt);
                else if (c == '-') st.push(lt - rt);
                else if (c == '*') st.push(lt * rt);
                else st.push(lt / rt);
            }
        }
        System.out.println(st.get(0));
    }
}
