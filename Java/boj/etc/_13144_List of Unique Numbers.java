import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        boolean[] visited = new boolean[100001];
        Arrays.fill(visited, false);
        int start = 0, end = 0;
        long answer = 0;
        while (start <= end && end < n) {
            if (!visited[arr[end]]) {
                visited[arr[end]] = true;
                end += 1;
                answer += end - start;
            } else {
                while (visited[arr[end]]) {
                    visited[arr[start]] = false;
                    start += 1;
                }
            }
        }
        System.out.println(answer);
    }
}
