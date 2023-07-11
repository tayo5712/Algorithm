package HashMap_TreeSet;

import java.util.HashMap;
import java.util.Scanner;

public class _04_01_학습회장 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        char[] ss = s.toCharArray();
        HashMap<Character, Integer> vote = new HashMap<>();
        for (int i = 0; i < n; i++) {
            vote.put(ss[i], vote.getOrDefault(ss[i], 0)+1);
//            if (!vote.containsKey(ss[i])) {
//                vote.put(ss[i], 1);
//            } else {
//                int score = vote.get(ss[i]);
//                vote.put(ss[i], ++score);
//            }
        }
        Character president = null;
        int maxValue = 0;
        for (Character key : vote.keySet()) {
            if (vote.get(key) > maxValue) {
                maxValue = vote.get(key);
                president = key;
            }
        }
        System.out.println(president);

    }
}
