import java.util.Scanner;

public class _1926_간단한369게임 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            int cnt = 0;
            for (char c : String.valueOf(i).toCharArray()) {
                if (c == '3' || c == '6' || c == '9') cnt++;
            }
            if (cnt > 0) {
                for (int j = 0; j < cnt; j++) {
                    System.out.print('-');
                }
            }
            else {
                System.out.print(i);
            }
            System.out.print(" ");
        }
    }
}
