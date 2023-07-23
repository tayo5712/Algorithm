package Recursive_Tree_Graph;

public class _07_02_이진수출력_재귀 {
    public void DFS(int n) {
        if (n == 0) {
            return;
        }
        else {
            DFS(n / 2);
            System.out.print(n % 2);
        }
    }

    public static void main(String[] args) {
        _07_02_이진수출력_재귀 T = new _07_02_이진수출력_재귀();
        T.DFS(11);
    }
}
