package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1090_체커 {
    static class Checker {
        int x;
        int y;
        public Checker(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Checker> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr.add(new Checker(x, y));
        }
        int[] answer = new int[N];
        Arrays.fill(answer, Integer.MAX_VALUE);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Checker center = new Checker(arr.get(i).x, arr.get(j).y);   // 거리 안에 있는 모든 점의 좌표를 모이는 점으로 설정
                int[] distance = new int[N];
                for (int k = 0; k < N; k++) {   // 모이는 점에서 모든 체커의 좌표까지의 거리를 저장
                    distance[k] = Math.abs(center.x - arr.get(k).x) + Math.abs(center.y - arr.get(k).y);
                }
                Arrays.sort(distance);  // 거리가 작은 순서대로 정렬
                int sumD = 0;
                for (int k = 0; k < N; k++) {
                    sumD += distance[k]; // 모이는 점으로 한개의 체커만 모일때.. 두개의 체커가 모일때 순으로 점점 더해줌
                    answer[k] = Math.min(answer[k], sumD); // 최소값 저장
                }
            }
        }
        for (int i = 0; i < N; i++) {
            System.out.print(answer[i] + " ");
        }
    }
}
