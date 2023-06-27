import java.util.Scanner;

public class _01_문자찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char c = sc.next().charAt(0);

        int result = 0;
        // 대, 소문자 구분 없으므로 전부 대문자로 바꾸기
        str = str.toUpperCase();
        c = Character.toUpperCase(c);

        for (char ch : str.toCharArray()) {
            if (ch == c) {
                result++;
            }
        }

        System.out.println(result);
    }
}
