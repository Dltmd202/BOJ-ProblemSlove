import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;
    private static int M;
    private static Node[][] map;
    private static boolean[][] lights;
    private static boolean[][] visited;
    private static int[] dy = {0, 0, -1, 1};
    private static int[] dx = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new Node[N + 1][N + 1];
        lights = new boolean[N + 1][N + 1];
        visited = new boolean[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N ; j++) {
                map[i][j] = new Node(i, j);
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Node cur = map[x][y];

            if(cur.isEmpty()){
                cur.lights = new ArrayList<>();
            }

            cur.lights.add(map[a][b]);
        }


        Queue<Node> q = new ArrayDeque<>();

        lights[1][1] = true;
        visited[1][1] = true;
        q.offer(map[1][1]);

        int res = 1;

        while (!q.isEmpty()){
            Node cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];

                if(1 > ny || ny > N || 1 > nx || nx > N) continue;

                map[ny][nx].canGo = true;
            }


            if(!cur.isEmpty()){
                for (Node next : cur.lights) {

                    if(!lights[next.y][next.x]){
                        lights[next.y][next.x] = true;
                        res++;
                    }

                    if(map[next.y][next.x].canGo && !visited[next.y][next.x]){
                        visited[next.y][next.x] = true;
                        q.offer(map[next.y][next.x]);
                    }
                }
            }

            for (int i = 0; i < 4; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];

                if(1 > ny || ny > N || 1 > nx || nx > N) continue;
                if(visited[ny][nx] || !map[ny][nx].canGo || !lights[ny][nx]) continue;

                visited[ny][nx] = true;
                q.offer(map[ny][nx]);
            }
            
        }

        System.out.println(res);
    }

    static class Node{
        int y;
        int x;
        List<Node> lights;
        boolean canGo;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }

        boolean isEmpty(){
            return lights == null;
        }
    }
}