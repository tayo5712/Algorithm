package Recursive_Tree_Graph;

import com.sun.tools.javac.Main;

class Node3 {
    int data;
    Node3 lt, rt;

    public Node3(int val) {
        data = val;
        lt = rt = null;
    }
}

public class _07_09_말단노드까지의가장짧은경로 {
    Node3 root;

    public int DFS(int L, Node3 root) {
        if (root.lt == null && root.rt == null) return L;
        else return Math.min(DFS(L + 1, root.lt), DFS(L + 1, root.rt));
    }
    public static void main(String[] args) {
        // DFS
        _07_09_말단노드까지의가장짧은경로 tree = new _07_09_말단노드까지의가장짧은경로();
        tree.root = new Node3(1);
        tree.root.lt = new Node3(2);
        tree.root.rt = new Node3(3);
        tree.root.lt.lt = new Node3(4);
        tree.root.lt.rt = new Node3(5);
        System.out.println(tree.DFS(0, tree.root));

    }
}
