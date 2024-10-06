package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.io.*;
import java.util.*;

public class _06_06_좌표정렬_복습 {
    static class point implements Comparable<point> {
        int x;
        int y;

        public point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(point p) {
            if (this.x == p.x) return this.y - p.y;
            return this.x - p.x;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<point> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr.add(new point(x, y));
        }
        Collections.sort(arr);
        for (point p : arr) {
            System.out.println(p.x + " " + p.y);
        }
    }
}
