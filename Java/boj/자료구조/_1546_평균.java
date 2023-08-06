package 자료구조;

import java.util.Scanner;

public class _1546_평균 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long sum = 0;
        long max = 0;

        for (int i=0; i<N; i++) {
            int num = sc.nextInt();
            if (num > max) {
                max = num;
            }
            sum += num;
        }
        sc.close();
        System.out.println(sum * 100.0 / max / N);
    }
}