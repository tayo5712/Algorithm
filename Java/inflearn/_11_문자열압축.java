import java.util.Scanner;

public class _11_문자열압축 {
    // 1
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        str += " ";
        String answer = "";
        int pos = 1;
        for (int i = 0; i < str.length()-1; i++) {
            if (str.charAt(i) == str.charAt(i + 1)) {
                pos++;
            } else {
                answer += str.charAt(i);
                if (pos > 1) {
                    answer += pos;
                }
                pos = 1;
            }
        }
        System.out.println(answer);
    }

// 2
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        String str = sc.next();
//        char now = '@';
//        int num = 0;
//        String answer = "";
//        for (char c : str.toCharArray()) {
//            if (now != c) {
//                now = c;
//                if (answer.length() > 0) {
//                    if (num > 1) {
//                        answer += num;
//                    }
//                }
//                answer += c;
//                num = 1;
//            } else {
//                num++;
//            }
//        }
//        if (num > 1) {
//            answer += num;
//        }
//        System.out.println(answer);
//    }
}
