import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, 1, -1};

    static enum Direction{
        UP, DOWN, RIGHT, LEFT
    }

    public static int getOrdinalTileType(char c){
        if(c == 'M') return 0;
        else if(c == '|') return 1;
        else if(c == '-') return 2;
        else if(c == '+') return 3;
        else if('1' <= c && c <= '3') return (c - '1' + 4);
        else return -1;
    }

    static Map<Character, int[]> moveType = new HashMap<>();
    static int[][] move = {
            {0, 1, 2, 3},
            {0, 1, -1, -1},
            {-1, -1, 2, 3},
            {0, 1, 2, 3},
            {2, -1, 1, -1},
            {-1, 2, 0, -1},
            {-1, 3, -1, 0},
            {2, -1, 1, -1}
    } ;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        char[][] map = new char[R + 1][C + 1];

        Node moscow = null;
        Node zagreb = null;
        Queue<Node> q = new ArrayDeque<>();

        for (int i = 0; i < R; i++) {
            char[] line = br.readLine().toCharArray();

            for (int j = 0; j < C; j++) {
                if(line[j] == 'M') {
                    q.offer(new Node(i, j, Direction.UP));
                    q.offer(new Node(i, j, Direction.DOWN));
                    q.offer(new Node(i, j, Direction.LEFT));
                    q.offer(new Node(i, j, Direction.RIGHT));
                }
                else if(line[j] == 'Z') zagreb = new Node(i, j);
            }
        }

        q.offer(moscow);

        while (!q.isEmpty()){
            Node cur = q.poll();
            int y = cur.y;
            int x = cur.x;
            int ordinalTile = getOrdinalTileType(map[y][x]);
            int ordinalDirection = cur.direction.ordinal();
            boolean res = false;

            for (Direction dir : Direction.values()) {
                int d = move[ordinalTile][dir.ordinal()];
            }

            for (int j = 0; j < 4; j++) {
                int d = move[ordinalTile][j];
                if(d == -1) continue;

                int ny = y + dy[d];
                int nx = x + dx[d];

                if(0 > ny || ny >= R || 0 > nx || nx >= C || map[ny][nx] == '.') continue;

                q.offer(new Node(ny, nx, cur.direction));
            }

            if(!res){

            }

        }
    }

    static class Node{
        int y;
        int x;
        Direction direction;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }

        public Node(int y, int x, Direction direction) {
            this.y = y;
            this.x = x;
            this.direction = direction;
        }
    }
}