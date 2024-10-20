import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] cows = br.readLine().toCharArray();
        int[] pos_st = new int[26];
        int[] pos_ed = new int[26];
        int cnt = 0;
        for (int i = 0; i < 52; i++) {
            if (pos_st[cows[i] - 'A'] == 0) {
                pos_st[cows[i] - 'A'] = i + 1;
            } else {
                pos_ed[cows[i] - 'A'] = i + 1;
            }
        }
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                if (pos_st[i] < pos_st[j] && pos_st[j] < pos_ed[i] && pos_ed[i] < pos_ed[j]) cnt++;
            }
        }
        System.out.println(cnt);

    }
}
