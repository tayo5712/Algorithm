package 자료구조;

import java.util.Scanner;

public class _11720_숫자의합구하기  {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String str = sc.next();
        int total = 0;

        char[] charArr = str.toCharArray();

        for (int i=0; i<N; i++) {
            total += charArr[i] - '0';

        }

//		for (int i=0; i<N; i++) {
//			total += Integer.parseInt(str.substring(i, i+1));
//		}

        System.out.println(total);

    }

}
