package Recursive_Tree_Graph;

import java.util.Scanner;

public class _07_01_재귀함수 {
    public void DFS(int n) {
        if (n == 0) {
            return;
        } else {
            DFS(n - 1);
            System.out.print(n + " ");
        }
    }

    public static void main(String[] args) {
        // 재귀함수를 이용하여 1부터 N까지를 출력하는 프로그램을 작성하세요
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        _07_01_재귀함수 T = new _07_01_재귀함수();
        T.DFS(n);
    }
}
