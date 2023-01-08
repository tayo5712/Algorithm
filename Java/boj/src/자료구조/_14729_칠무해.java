package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _14729_칠무해 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        double[] students = new double[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            students[i] = Double.parseDouble(st.nextToken());
        }
        Arrays.sort(students);
        for (int i = 0; i < 7; i++) {
            System.out.printf("%.3f\n", students[i]);
        }
    }
}
