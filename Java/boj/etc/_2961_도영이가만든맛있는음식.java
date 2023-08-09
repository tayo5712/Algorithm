package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _2961_도영이가만든맛있는음식 {
    static int answer = Integer.MAX_VALUE;
    static int[] used;
    static ArrayList<ingredient> box;
    static int N;

    static class ingredient {
        int sour;
        int bitter;
        public ingredient(int sour, int bitter) {
            this.sour = sour;
            this.bitter = bitter;
        }
    }

    static void DFS(int L) {
        if (L == N) {
            int sumS = 1;
            int sumB = 0;
            for (int i = 0; i < N; i++) {
                if (used[i] == 1) {
                    sumS *= box.get(i).sour;
                    sumB += box.get(i).bitter;
                }
            }
            if (sumB > 0) answer = Math.min(answer, Math.abs(sumS - sumB));
        }
        else {
            used[L] = 1;
            DFS(L + 1);
            used[L] = 0;
            DFS(L + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        box = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            box.add(new ingredient(a, b));
        }
        used = new int[N];
        DFS(0);
        System.out.println(answer);
    }
}
