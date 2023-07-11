package HashMap_TreeSet;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class _04_03_매출액의종류 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] sales = new int[n];
        for (int i = 0; i < n; i++) {
            sales[i] = sc.nextInt();
        }
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<Integer, Integer> salesMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (i < k) {
                salesMap.put(sales[i], salesMap.getOrDefault(sales[i], 0) + 1);
                if (i + 1 == k) {
                    answer.add(salesMap.size());
                }
            } else {
                salesMap.put(sales[i], salesMap.getOrDefault(sales[i], 0) + 1);
                if (salesMap.get(sales[i - k]) > 1) salesMap.put(sales[i - k], salesMap.get(sales[i - k]) - 1);
                else salesMap.remove(sales[i - k]);
                answer.add(salesMap.size());
            }
        }
        for (int i : answer) {
            System.out.print(i + " ");
        }
    }
}
