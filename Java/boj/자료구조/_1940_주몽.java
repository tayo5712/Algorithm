package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1940_주몽 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);   // 정렬
        int a = 0;
        int b = N-1;
        int count = 0;
        while (a < b) {
            if (arr[a] + arr[b] == M) {count++; a++; b--;}  // 목표 값이 나오면 인덱스를 둘다 바꾼다.
            else if (arr[a] + arr[b] < M) a++; // 목표 값보다 작으면 왼쪽 인덱스에 1을 더해 크기를 늘려준다.
            else b--; // 목표 값보다 크면 오른쪽 인덱스에 1을 빼서 크기를 줄여준다.
        }
        System.out.println(count);

    }
}
