import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[][] map;
    private static int[][] dist;
    private static final int[] dx = {0, 0, 1, -1};
    private static final int[] dy = {1, -1, 0 ,0};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        dist = new int[N][N];

        for(int i = 0; i < N; i ++){
            String line = br.readLine();
            int j = 0;
            for(char ch: line.toCharArray()){
                map[i][j] = ch - '0';
                dist[i][j] = Integer.MAX_VALUE;
                j ++;
            }
        }

        bfs();
        System.out.println(dist[N - 1][N - 1]);
    }

    private static void bfs(){
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0));
        dist[0][0] = 0;

        while(!q.isEmpty()){
            Node now = q.poll();

            for(int i = 0; i < 4; i ++){
                int ny = now.y + dy[i];
                int nx = now.x + dx[i];
                if(0 <= ny && ny < N && 0 <= nx && nx < N && dist[ny][nx] > dist[now.y][now.x]){
                    if(map[ny][nx] == 1) {
                        dist[ny][nx] = dist[now.y][now.x];
                    } else {
                        dist[ny][nx] = dist[now.y][now.x] + 1;
                    }
                    q.offer(new Node(ny, nx));
                }
            }
        }
    }

    public static class Node{
        int x;
        int y;

        public Node(int y, int x) {
            this.x = x;
            this.y = y;
        }
    }
}
