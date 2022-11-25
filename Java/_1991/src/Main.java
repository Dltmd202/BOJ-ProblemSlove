import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Node nodes[] = new Node[n];

        for (int i = 0; i < n; i++) {
            nodes[i] = new Node();
            nodes[i].val = (char) ('A' + i);
        }

        for (int i = 0; i < n; i++) {
            char[] data = br.readLine().toCharArray();
            char parent = data[0];
            char left = data[2];
            char right = data[4];

            if(left != '.')
                nodes[getIdx(parent)].left = nodes[getIdx(left)];
            if(right != '.')
                nodes[getIdx(parent)].right = nodes[getIdx(right)];
        }

        preorder(nodes[0], sb);
        System.out.println(sb.toString().trim());
        sb = new StringBuilder();
        inorder(nodes[0], sb);
        System.out.println(sb.toString().trim());
        sb = new StringBuilder();
        postorder(nodes[0], sb);
        System.out.println(sb.toString().trim());
    }

    public static void preorder(Node cur, StringBuilder sb){
        if(cur == null) return;
        sb.append(cur.val);
        preorder(cur.left, sb);
        preorder(cur.right, sb);
    }

    public static void inorder(Node cur, StringBuilder sb){
        if(cur == null) return;
        inorder(cur.left, sb);
        sb.append(cur.val);
        inorder(cur.right, sb);
    }

    public static void postorder(Node cur, StringBuilder sb){
        if(cur == null) return;
        postorder(cur.left, sb);
        postorder(cur.right, sb);
        sb.append(cur.val);
    }

    public static int getIdx(char c){
        return c - 'A';
    }

    static class Node{
        char val;
        Node left;
        Node right;
    }
}