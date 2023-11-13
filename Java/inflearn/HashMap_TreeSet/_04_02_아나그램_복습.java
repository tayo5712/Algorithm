package HashMap_TreeSet;

import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class _04_02_아나그램_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] s1 = sc.next().toCharArray();
        char[] s2 = sc.next().toCharArray();
        HashMap<Character, Integer> hm1 = new HashMap<>();
        HashMap<Character, Integer> hm2 = new HashMap<>();
        for (char c : s1) {
            hm1.put(c, hm1.getOrDefault(c, 0) + 1);
        }
        for (char c : s2) {
            hm2.put(c, hm2.getOrDefault(c, 0) + 1);
        }
        if (hm1.equals(hm2)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
