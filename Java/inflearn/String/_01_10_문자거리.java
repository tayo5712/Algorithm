package String;

import java.util.Scanner;

public class _01_10_문자거리 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 1
        String str = sc.next();
        char c = sc.next().charAt(0);
        int[] answer = new int[str.length()];
        int p = 1000;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == c) {
                p = 0;
                answer[i] = p;
            } else {
                p++;
                answer[i] = p;
            }
        }

        p = 1000;
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) == c) {
                p = 0;
                answer[i] = p;
            } else {
                p++;
                answer[i] = Math.min(answer[i], p);
            }
        }
        for (int i : answer) {
            System.out.print(i + " ");
        }




        // 2
//        String words = sc.next();
//        String target = sc.next();
//        int[] arr = new int[words.length()];
//        Arrays.fill(arr, 101);
//        int pos = 0;
//        while (words.indexOf(target, pos) != -1) {
//            pos = words.indexOf(target, pos);
//            for (int i=0; i < arr.length; i++) {
//                int x = Math.abs(pos - i);
//                arr[i] = (x < arr[i]) ? x : arr[i];
//            }
//            pos++;
//        }
//        for (int i : arr) {
//            System.out.print(i + " ");
//        }
    }
}
