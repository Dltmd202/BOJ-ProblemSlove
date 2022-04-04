import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;


public class Main {

    static class Point{
        int x;
        int y;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "Point{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int[] tree;
    static int T;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());

        while(T --> 0){
            int n = Integer.parseInt(br.readLine());

            List<Point> points = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                points.add(new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
            }

            Collections.sort(points, (p1, p2) -> p2.y - p1.y);

            int[] ret = new int[n];
            int cnt = 1;
            for (int i = 0; i < n; i++) {
                if(i > 0 && points.get(i).y != points.get(i - 1).y) cnt++;
                ret[i] = cnt;
            }

            for (int i = 0; i < n; i++) {
                points.get(i).y = ret[i];
            }

            Collections.sort(points, (p1, p2) -> {
                if(p1.x == p2.x) return p1.y - p2.y;
                else return p1.x - p2.x;
            });


            tree = new int[n * 4];
            long res = 0;
            for (int i = 0; i < n; i++) {
                res += query(1, n, 1, 1, points.get(i).y);
                update(1, n, 1, points.get(i).y);
            }
            sb.append(res).append("\n");
        }
        System.out.println(sb.toString());


    }

    private static void update(int start, int end, int node, int idx) {
        if(idx < start || end < idx) return;
        tree[node] += 1;
        if(start == end) return;
        int mid = (start + end) / 2;
        update(start, mid, node * 2, idx);
        update(mid + 1, end, node * 2 + 1, idx);
    }

    private static long query(int start, int end, int node, int left, int right) {
        if(end < left || right < start) return 0;
        if(left <= start && end <= right) return tree[node];
        int mid = (start + end) / 2;
        return query(start, mid, node * 2, left, right) +
                query(mid + 1, end, node * 2 + 1, left, right);
    }
}
