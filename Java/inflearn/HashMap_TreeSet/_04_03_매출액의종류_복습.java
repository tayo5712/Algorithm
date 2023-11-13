package HashMap_TreeSet;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class _04_03_매출액의종류_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        HashMap<Integer, Integer> hm = new HashMap<>();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i < k) {
                hm.put(arr[i], hm.getOrDefault(arr[i], 0) + 1);
                if (i + 1 == k) {
                    list.add(hm.size());
                }
            }
            else {
                hm.put(arr[i], hm.getOrDefault(arr[i], 0) + 1);
                if (hm.get(arr[i - k]) > 1) hm.put(arr[i - k], hm.get(arr[i - k]) - 1);
                else hm.remove(arr[i - k]);
                list.add(hm.size());
            }
        }
        for (int i : list) System.out.print(i + " ");
    }
}
