import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringBuilder sb = new StringBuilder();
    static int[] data;
    static int[] tree;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        data = new int[N + 1];
        tree = new int[N * 4];
        for (int i = 1; i < N + 1; i++) {
            data[i] = Integer.parseInt(br.readLine());
        }

        initTree(1, N, 1);

        for(int i = 0; i < M; i ++){
            st = new StringTokenizer(br.readLine());

            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            sb.append(query(1, N, 1, left, right)).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static int initTree(int start, int end, int node){
        if(start == end){
            return tree[node] = data[start];
        }
        int mid = (start + end) / 2;
        return tree[node] = Math.min(
                initTree(start, mid, node * 2),
                initTree(mid + 1, end, node * 2 + 1));
    }

    public static int query(int start, int end, int node, int left, int right){
        if(right < start || end < left){
            return Integer.MAX_VALUE;
        }
        if(left <= start && end <= right){
            return tree[node];
        }
        int mid = (start + end) / 2;

        return Math.min(
                query(start, mid, node * 2, left, right),
                query(mid + 1, end, node * 2 + 1, left, right)
        );
    }
}
