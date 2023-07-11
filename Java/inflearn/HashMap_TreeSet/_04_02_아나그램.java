package HashMap_TreeSet;

import java.util.HashMap;
import java.util.Scanner;

public class _04_02_아나그램 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        char[] aChar = a.toCharArray();
        char[] bChar = b.toCharArray();
        HashMap<Character, Integer> ahash = new HashMap<>();
        HashMap<Character, Integer> bhash = new HashMap<>();

        for (int i = 0; i < aChar.length; i++) {
            ahash.put(aChar[i], ahash.getOrDefault(aChar[i], 0) + 1);
            bhash.put(bChar[i], bhash.getOrDefault(bChar[i], 0) + 1);
        }
        if (ahash.equals(bhash)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
