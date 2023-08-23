package etc;

import java.util.*;

public class _2212_센서 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        HashSet<Integer> hs = new HashSet<>();
        for (int i = 0; i < n; i++) {
            hs.add(sc.nextInt());
        }
        ArrayList<Integer> arr = new ArrayList<>(hs);
        Collections.sort(arr);

        if (k >= n) System.out.println(0);
        else {
            ArrayList<Integer> distance = new ArrayList<>();
            for (int i = 1; i < arr.size(); i++) {
                distance.add(arr.get(i) - arr.get(i - 1));
            }
            Collections.sort(distance);
            int answer = 0;
            for (int i = 0; i < distance.size()-(k-1); i++) {
                answer += distance.get(i);
            }
            System.out.println(answer);
        }
    }
}
