package Sorting_Searching_정렬_이분검색_결정알고리즘;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Point implements Comparable<Point> {
    public int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    @Override
    public int compareTo(Point o) {
        if (this.x == o.x) return this.y-o.y;
        // 음수가 리턴이 되면 매개변수로 들어오는 객체가 현재 객체 다음 (this -> o)
        return this.x-o.x;
    }
}

public class _06_07_좌표정렬_compareTo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Point> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            arr.add(new Point(x, y));
        }
        Collections.sort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr.get(i).x + " " + arr.get(i).y);
        }
    }
}
