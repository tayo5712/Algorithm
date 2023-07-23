package Recursive_Tree_Graph;

public class _07_04_피보나치재귀 {
    static int[] memo;
    public int DFS(int n) {
        if (memo[n] != 0) return memo[n];
        if (n == 1) return memo[n] = 1;
        else if (n == 2) return memo[n] = 1;
        else return memo[n] = DFS(n-2) + DFS(n-1);
    }
    public static void main(String[] args) {
        _07_04_피보나치재귀 T = new _07_04_피보나치재귀();
        int n = 45;
        memo = new int[n+1];
        T.DFS(n);
        for (int i = 1; i <= n; i++) {
            System.out.print(memo[i] + " ");
        }
    }
}
