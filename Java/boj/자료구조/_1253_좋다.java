package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1253_좋다 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long arr[] = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int result = 0;
        for (int i = 0; i < N; i++) {
            int a = 0;
            int b = N-1;
            long find = arr[i];
            while (a < b) { // a가 b보다 작을 동안
                if (arr[a] + arr[b] == find) {  // 두 값을 더한 것이 목표 값이면
                    if (a != i && b != i) { // 만약 두 인덱스가 목표값의 인덱스와 다르다면 정답에 1을 더해줌
                        result++;
                        break;
                    }
                    if (a == i) {   // 왼쪽 인덱스가 목표값 인덱스와 같다면 인덱스를 1 늘려 줌
                        a++;
                    } else {    // 오른쪽 인덱스가 목표값 인덱스와 같다면 인덱스를 1 줄여 줌
                        b--;
                    }
                }
                else if(arr[a] + arr[b] < find) {   // 두 값을 더한 것이 목표 값 보다 작으면 왼쪽 인덱스 값을 1늘려 줌
                    a++;
                } else {    // 두 값을 더한 것이 목표 값 보다 크면 오른쪽 인덱스 값을 1줄여 줌
                    b--;
                }
            }
        }
        System.out.println(result);
    }
}
