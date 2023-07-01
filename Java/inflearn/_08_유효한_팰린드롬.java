import java.util.Scanner;

public class _08_유효한_팰린드롬 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String tmp = new StringBuilder(s).reverse().toString();
        // 1
        s = s.replaceAll("[^a-zA-Z]", "");
        if (s.equalsIgnoreCase(tmp)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        // 2
//        char[] ca = s.toCharArray();
//        StringBuilder sb = new StringBuilder();
//        for (char c : ca ) {
//            if (Character.isAlphabetic(c)) {
//                sb.append(c);
//            }
//        }
//        if (sb.toString().equalsIgnoreCase(sb.reverse().toString())) {
//            System.out.println("YES");
//        } else {
//            System.out.println("NO");
//        }
    }
}
