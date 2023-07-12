package HashMap_TreeSet;

import java.util.*;

public class _04_05_K번째큰수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // TreeSet은 중복제거, 자동 정렬까지 해줌
        TreeSet<Integer> set = new TreeSet<>(Collections.reverseOrder());

        for (int i = 0; i < n-2; i++) {
            for (int j = i+1; j < n-1; j++) {
                for (int l = j+1; l < n; l++) {
                    set.add(arr[i] + arr[j] + arr[l]);
                }
            }
        }
        if (set.size() >= k) {
            int cnt = 0;
            for (int i : set) {
                cnt++;
                if (cnt == k) {
                    System.out.println(i);
                }
            }
        } else System.out.println(-1);
    }
}
