package HashMap_TreeSet;

import java.util.HashMap;
import java.util.Scanner;

public class _04_01_학습회장_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        char[] result = s.toCharArray();
        HashMap<Character, Integer> vote = new HashMap<>();
        for (char candidate : result) {
            vote.put(candidate, vote.getOrDefault(candidate,0) + 1);
        }
        Character president = null;
        int maxV = 0;
        for (char candidate : vote.keySet()) {
            if (vote.get(candidate) > maxV) {
                maxV = vote.get(candidate);
                president = candidate;
            }
        }
        System.out.println(president);
    }
}
