package Recursive_Tree_Graph;

import java.util.LinkedList;
import java.util.Queue;

public class _07_10_말단노드까지의가장짧은경로_BFS {
    Node3 root;

    public int BFS(Node3 root) {
        Queue<Node3> q = new LinkedList<>();
        int L = 0;
        q.offer(root);
        while (!q.isEmpty()) {
            int len = q.size();
            for (int i = 0; i < len; i++) {
                Node3 n3 = q.poll();
                if (n3.lt == null && n3.rt == null) return L;
                if (n3.lt != null) q.offer(n3.lt);
                if (n3.rt != null) q.offer(n3.rt);
            }
            L++;
        }
        return 0;
    }
    public static void main(String[] args) {
        // BFS
        _07_10_말단노드까지의가장짧은경로_BFS tree = new _07_10_말단노드까지의가장짧은경로_BFS();
        tree.root = new Node3(1);
        tree.root.lt = new Node3(2);
        tree.root.rt = new Node3(3);
        tree.root.lt.lt = new Node3(4);
        tree.root.lt.rt = new Node3(5);
        System.out.println(tree.BFS(tree.root));
    }
}
