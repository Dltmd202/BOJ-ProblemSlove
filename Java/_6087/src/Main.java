import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dy = {-1, 1, 0, 0, 0};
    static int[] dx = {0, 0, -1, 1, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        char[][] map = new char[H][W];
        Node[] connections = new Node[2];
        int cursor = 0;


        for (int i = 0; i < H; i++) {
            char[] line = br.readLine().toCharArray();
            map[i] = line;
            for (int j = 0; j < W; j++) {
                if(map[i][j] == 'C'){
                    connections[cursor++] = new Node(i, j, Node.DIR.NO, 0);
                }
            }
        }

        int[][] visited = new int[H][W];
        for (int i = 0; i < H; i++) {
            Arrays.fill(visited[i], Integer.MAX_VALUE);
        }
        visited[connections[0].y][connections[0].x] = 0;
        int res = Integer.MAX_VALUE;
        Queue<Node> q = new ArrayDeque<>();
        q.offer(connections[0]);

        while (!q.isEmpty()){
            Node cur = q.poll();

            if(cur.equals(connections[1])){
                res = Math.min(res, cur.mirror);
            }

            for (Node.DIR dir : Node.DIR.values()) {
                int ny = cur.y + dy[dir.ordinal()];
                int nx = cur.x + dx[dir.ordinal()];

                if(0 > ny || ny >= H || 0 > nx || nx >= W || dir == Node.DIR.NO)
                    continue;

                if(map[ny][nx] == '*')
                    continue;

                if(cur.direction == dir || cur.direction == Node.DIR.NO){
                    if(visited[ny][nx] >= cur.mirror) {
                        q.offer(new Node(ny, nx, dir, cur.mirror));
                        visited[ny][nx] = cur.mirror;
                    }
                } else {
                    if(visited[ny][nx] >= cur.mirror + 1) {
                        q.offer(new Node(ny, nx, dir, cur.mirror + 1));
                        visited[ny][nx] = cur.mirror + 1;
                    }
                }
            }
        }
        System.out.println(res);
    }

    static class Node{
        enum DIR {UP, DOWM, LEFT, RIGHT, NO};
        int y;
        int x;
        DIR direction;
        int mirror;

        @Override
        public boolean equals(Object obj) {
            Node other = (Node) obj;
            return this.y == other.y && this.x == other.x;
        }

        public Node(int y, int x, DIR dir, int mirror) {
            this.y = y;
            this.x = x;
            this.direction = dir;
            this.mirror = mirror;
        }
    }
}