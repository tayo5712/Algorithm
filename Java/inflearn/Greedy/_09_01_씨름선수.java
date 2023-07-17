package Greedy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Person implements Comparable<Person>{
    int h;
    int w;
    public Person(int h, int w) {
        this.h = h;
        this.w = w;
    }

    @Override
    public int compareTo(Person o) {
        return o.h - this.h;
    }
}

public class _09_01_씨름선수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Person> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int h = sc.nextInt();
            int w = sc.nextInt();
            arr.add(new Person(h, w));
        }
        Collections.sort(arr);
        int cnt = 0;
        int maxW = 0;
        for (int i = 0; i < n; i++) {
            if (arr.get(i).w > maxW) {
                maxW = arr.get(i).w;
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
