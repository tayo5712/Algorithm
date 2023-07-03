package String;

import java.util.Scanner;

public class _01_05_특정_문자_뒤집기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String words = sc.next();
        char[] list = words.toCharArray();
        int lt = 0;
        int rt = list.length - 1;
        while (lt < rt) {
            if (!Character.isLetter(list[lt])) {
                lt++;
            } else if (!Character.isLetter(list[rt])) {
                rt--;
            } else {
                char temp = list[rt];
                list[rt] = list[lt];
                list[lt] = temp;
                lt++;
                rt--;
            }
        }
        System.out.println(String.valueOf(list));
    }
}
