import java.util.Scanner;

public class _12_암호 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String password = sc.next();
        password = password.replace('#', '1').replace('*', '0');
        String answer = "";
        for (int i = 0; i < n; i++) {
            String code = password.substring(0, 7);
            password = password.substring(7);
            int decimal = Integer.parseInt(code, 2);
            answer += (char) decimal;
        }
        System.out.println(answer);
    }
}
