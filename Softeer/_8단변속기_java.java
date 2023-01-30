import java.util.Scanner;

public class _8단변속기_java {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String answer = sc.nextLine();
        String ascending = "1 2 3 4 5 6 7 8";
        String descending = "8 7 6 5 4 3 2 1";
        if (answer.equals(ascending)) {
            System.out.println("ascending");
        } else {
            if (answer.equals(descending)) {
                System.out.println("descending");
            } else {
                System.out.println("mixed");
            }
        }
    }
}

