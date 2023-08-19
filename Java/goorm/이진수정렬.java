import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class 이진수정렬 {
    static class Pair implements Comparable<Pair>{
        int num;
        int bit;
        public Pair(int num, int bit) {
            this.num = num;
            this.bit = bit;
        }
        @Override
        public int compareTo(Pair o) {
            if (this.bit == o.bit) return o.num - this.num;
            return o.bit - this.bitㅎ;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        ArrayList<Pair> pairs = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            int bit = Integer.bitCount(num);
            pairs.add(new Pair(num, bit));
        }
        Collections.sort(pairs);
        System.out.println(pairs.get(k-1).num);
    }
}
