import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static long[] tree;

    public static void main(String[] args) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        tree = new long[n * 4];

        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < m; i ++){
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0){
                if(b > c){
                    int temp = b;
                    b = c;
                    c = temp;
                }
                sb.append(query(1, n, 1, b,c)).append("\n");
            } else if (a == 1){
                update(1, n,1, b, c);
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
    public static long query(int start, int end, int node, int left, int right){
        if (left > end || start > right) return 0;

        if (left <= start && end <= right) return tree[node];

        int mid = (start + end) / 2;
        long left_ = query(start, mid, node * 2, left, right);
        long right_ = query(mid + 1, end, node * 2 + 1, left, right);
        return left_ + right_;
    }

    public static long update(int start, int end, int node, int idx, int val){
        if (idx < start || idx > end) return tree[node];

        if (start == end) {
            tree[node] = val;
            return tree[node];
        }

        int mid = (start + end) / 2;
        tree[node] = update(start, mid, node * 2, idx, val) + update(mid + 1, end, node * 2 + 1, idx, val);
        return tree[node];
    }
}
