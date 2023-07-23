package Recursive_Tree_Graph;

import com.sun.tools.javac.Main;

public class _07_03_팩토리얼 {
    public int DFS(int n) {
        if (n == 1) return n;
        return n * DFS(n-1);
    }
    public static void main(String[] args) {
        _07_03_팩토리얼 T = new _07_03_팩토리얼();
        System.out.println(T.DFS(6));
    }
}
