package etc;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(0);
        for (int i = 1; i < 200; i++) {
            for (int j = 0; j < i; j++) {
                arr.add(i);
            }
        }
        int answer = 0;
        for (int i = n; i < m + 1; i++) {
            answer += arr.get(i);
        }
        System.out.println(answer);
    }
}
