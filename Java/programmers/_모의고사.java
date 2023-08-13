import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[] collect = new int[4];
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == one[i % one.length]) {
                collect[1] += 1;
            }
            if (answers[i] == two[i % two.length]) {
                collect[2] += 1;
            }
            if (answers[i] == three[i % three.length]) {
                collect[3] += 1;
            }
        }
        int maxV = 0;
        for (int i = 1; i < 4; i++) {
            if (collect[i] > maxV) maxV = collect[i];
        }
        for (int i = 1; i < 4; i++) {
            if (collect[i] == maxV) answer.add(i);
        }
        return answer;
    }
}