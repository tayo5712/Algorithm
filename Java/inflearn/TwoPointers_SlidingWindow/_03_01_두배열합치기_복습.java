package TwoPointers_SlidingWindow;

import java.util.Scanner;

public class _03_01_두배열합치기_복습 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] n_arr = new int[n];
        for (int i = 0; i < n; i++) {
            n_arr[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        int[] m_arr = new int[m];
        for (int i = 0; i < m; i++) {
            m_arr[i] = sc.nextInt();
        }
        int[] result = new int[n + m];
        int n_point = 0;
        int m_point = 0;
        int i = 0;
        while (n_point < n && m_point < m) {
            if (n_arr[n_point] <= m_arr[m_point]) {
                result[i] = n_arr[n_point];
                i++;
                n_point++;
            } else {
                result[i] = m_arr[m_point];
                i++;
                m_point++;
            }
        }
        while (n_point < n) {
            result[i] = n_arr[n_point];
            i++;
            n_point++;
        }
        while (m_point < m) {
            result[i] = m_arr[m_point];
            i++;
            m_point++;
        }
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
