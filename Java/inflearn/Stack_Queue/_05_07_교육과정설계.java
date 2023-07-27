package Stack_Queue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class _05_07_교육과정설계 {
    public static void main(String[] args) {
        // Queue로 풀어보기
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();

        String answer = "YES";
        Queue<Character> Q = new LinkedList<>();
        for (char x : a.toCharArray()) {
            Q.offer(x);
        }
        for (char x : b.toCharArray()) {
            if (Q.contains(x)) {
                if (x != Q.poll()) {
                    answer = "NO";
                    break;
                }
            }
        }
        if (!Q.isEmpty()) answer = "NO";
        System.out.println(answer);

//        Scanner sc = new Scanner(System.in);
//        String necS = sc.nextLine();
//        char[] nec = necS.toCharArray();
//        String struct = sc.nextLine();
//        char[] str = struct.toCharArray();
//        int index = 0;
//        for (int i = 0; i < str.length; i++) {
//            if (index < nec.length && nec[index] == str[i]) index++;
//        }
//        if (index == nec.length) System.out.println("YES");
//        else System.out.println("NO");
    }
}
