import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static long res;
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder sb = new StringBuilder();
    private static int[] tree;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        tree = new int[N * 4];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] data = new int[N + 1];

        for (int i = 1; i < N + 1; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = N; i > 0; i--) {
            res += query(1, N, 1, 1, data[i] - 1);
            update(1, N, 1, data[i]);
        }
        System.out.println(res);
    }

    public static int update(int start, int end, int node, int idx){
        if(idx < start || end < idx) return tree[node];
        if(start == end) {
            tree[node] += 1;
            return tree[node];
        }

        int mid = (start + end) / 2;
        tree[node] = update(start, mid, node * 2, idx) + update(mid + 1, end, node * 2 + 1, idx);
        return tree[node];
    }

    public static int query(int start, int end, int node, int left, int right){
        if (right < start || end < left) return 0;
        if (left <= start && end <= right) return tree[node];
        int mid = (start + end) / 2;
        return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right);
    }
}