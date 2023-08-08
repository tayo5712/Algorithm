package etc;

import java.util.Scanner;

public class _14568_2017_연세대학교_프로그래밍_경시대회 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        int N = sc.nextInt();
        for (int i = 1; i < N; i++) {   // 남규
            for (int j = 1; j < N; j++) {   // 영훈
                for (int k = 1; k < N; k++) {   // 택희
                    if (i >= j+2 && k % 2 == 0 && i + j + k == N) {
                        answer += 1;
                    }
                }
            }
        }
        System.out.println(answer);
        // 남규 >= 영훈 + 2
        // 남규 != 0 && 영훈 != 0 && 택희 != 0
        // 택희 % 2 == 0
    }
}
