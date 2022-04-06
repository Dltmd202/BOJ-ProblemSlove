import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder sb = new StringBuilder();
    private static final int MAX = 2_000_000;
    private static final int[] tree = new int[MAX * 4 + 1];
    private static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            int data = Integer.parseInt(st.nextToken());
            if (type == 1){
                update(1, MAX, 1, data);
            } else {
                sb.append(query(1, MAX, 1, data))
                        .append("\n");
            }
        }
        System.out.println(sb.toString().trim());
    }

    public static void update(int start, int end, int node, int idx){
        if(end < idx || idx < start){
            return;
        }
        tree[node] += 1;
        if(start == end) return;
        int mid = (start + end) / 2;

        update(start, mid, node * 2, idx);
        update(mid + 1, end, node * 2 + 1, idx);
    }

    public static int query(int start, int end, int node, int data){
        tree[node] -= 1;
        if(start == end){
            return start;
        }
        int mid = (start + end) / 2;
        if (tree[node * 2] < data){
            return query(mid + 1, end, node * 2 + 1, data - tree[2 * node]);
        } else{
            return query(start, mid, 2 * node, data);
        }
    }
}
