package HashMap_TreeSet;

import java.util.HashMap;
import java.util.Scanner;

public class _04_04_모든아나그램찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        String T = sc.next();
        char[] S_Char = S.toCharArray();
        char[] T_Char = T.toCharArray();

        HashMap<Character, Integer> S_Hash = new HashMap<>();
        HashMap<Character, Integer> T_Hash = new HashMap<>();
        for (int i = 0; i < T_Char.length; i++) {
            T_Hash.put(T_Char[i], T_Hash.getOrDefault(T_Char[i], 0) + 1);
        }
        int answer = 0;
        for (int i = 0; i < S_Char.length; i++) {
            if (i < T_Char.length) {
                S_Hash.put(S_Char[i], S_Hash.getOrDefault(S_Char[i], 0) + 1);
                if (i + 1 == T_Char.length) {
                    if (S_Hash.equals(T_Hash)) answer++;
                }
            } else {
                S_Hash.put(S_Char[i], S_Hash.getOrDefault(S_Char[i], 0) + 1);
                if (S_Hash.get(S_Char[i - T_Char.length]) > 1)
                    S_Hash.put(S_Char[i - T_Char.length], S_Hash.get(S_Char[i - T_Char.length]) - 1);
                else S_Hash.remove(S_Char[i - T_Char.length]);
                if (S_Hash.equals(T_Hash)) answer++;
            }
        }
        System.out.println(answer);
    }
}
