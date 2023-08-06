package 자료구조;

import java.util.Scanner;

public class _2018_수들의합5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int sum = 1;
        int cnt = 1; // N 하나 뽑을 경우의 수로 초기화
        int st = 1;
        int ed = 1;
        while (ed != N) {   // 마지막 인덱스랑 N값이 같지 않을 때만
            if (sum == N) { // 연속된 수의 합이 N일 경우 cnt값을 1 더해주고 마지막 인덱스도 1더해주면 수의 합에 마지막 인덱스 값도 더해준다.
                cnt++;
                ed++;
                sum += ed;
            } else if (sum > N) {   // 연속된 수의 합이 N보다 클경우 합에서 시작 인덱스 값을 빼고 시작 인덱스 값을 1더해준다.
                sum -= st;
                st++;
            } else { // 연속된 수의 합이 N보다 작을 경우 마지막 인덱스 값을 1 더해주고 그 값을 합에 더해준다.
                ed++;
                sum += ed;
            }
        }
        System.out.println(cnt);
    }
}
