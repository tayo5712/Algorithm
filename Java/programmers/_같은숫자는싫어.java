import java.util.ArrayList;
import java.util.Stack;

public class _같은숫자는싫어 {
    public ArrayList<Integer> solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        Stack<Integer> st = new Stack<>();
        for (int n : arr) {
            if (!st.isEmpty()) {
                if (st.peek() != n) st.push(n);
            }
            else {
                st.push(n);
            }
        }
        for (int n : st) answer.add(n);
        return answer;
    }
}
