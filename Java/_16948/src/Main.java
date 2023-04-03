import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int[] dy = {-2, -2, 0, 0, 2, 2};
    private static int[] dx = {-1, 1, -2, 2, -1, 1};
    private static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        visited = new boolean[N + 1][N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        Node start = new Node(
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()),
                0
        );

        Node dest = new Node(
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()),
                Integer.MAX_VALUE
        );

        System.out.println(search(start, dest));

    }

    private static int search(Node start, Node dest) {
        Queue<Node> q = new ArrayDeque<>();
        visited[start.y][start.x] = true;

        q.offer(start);



        while (!q.isEmpty()){
            Node cur = q.poll();

            if(cur.y == dest.y && cur.x == dest.x){
                return cur.cnt;
            }

            for (int i = 0; i < 6; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];

                if(0 <= ny && ny <= N && 0 <= nx && nx <= N && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    q.offer(new Node(ny, nx, cur.cnt + 1));
                }
            }
        }
        return -1;
    }

    static class Node{
        int y;
        int x;
        int cnt;

        public Node(int y, int x, int cnt) {
            this.y = y;
            this.x = x;
            this.cnt = cnt;
        }
    }

}