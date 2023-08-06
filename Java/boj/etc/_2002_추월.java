package etc;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class _2002_추월 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Queue<String> q = new LinkedList<>();
        int answer = 0;
        for (int i = 0; i < n; i++) {
            String a = br.readLine();
            q.offer(a);
        }
        String origin = q.poll();
        for (int i = 0; i < n; i++) {
            String now = br.readLine();
            if (origin.equals(now)) origin = q.poll();
            else {
                answer++;
                q.remove(now);
            }
        }
        System.out.println(answer);
    }
}
