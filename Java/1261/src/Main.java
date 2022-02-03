import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[][] map;
    static int[][] broken;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        broken = new int[N][M];

        for (int i = 0; i < N; i++) {
            Arrays.fill(broken[i], Integer.MAX_VALUE);
        }

        for(int i = 0; i < N; i ++){
            int j = 0;
            for (char c : br.readLine().toCharArray()) {
                map[i][j] = c - '0';
                j ++;
            }
        }
        Queue<Node> q = new PriorityQueue<>(new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.cnt >= o2.cnt ? 1: -1;
            }
        });
        broken[0][0] = 0;
        q.offer(new Node(0, 0, 0));

        while(!q.isEmpty()){
            Node now = q.poll();

            if(now.y == N - 1 && now.x == M - 1){
                System.out.println(now.cnt);
                break;
            }

            for(int i = 0; i < 4; i ++){
                int ny = now.y + dy[i];
                int nx = now.x + dx[i];

                if(0 <= ny && ny < N && 0 <= nx && nx < M){
                    if(map[ny][nx] == 0) {
                        if (broken[ny][nx] > now.cnt) {
                            broken[ny][nx] = now.cnt;
                            q.offer(new Node(now.cnt, ny, nx));
                        }
                    } else {
                        if(broken[ny][nx] > now.cnt + 1){
                            broken[ny][nx] = now.cnt + 1;
                            q.offer(new Node(now.cnt + 1, ny, nx));
                        }
                    }
                }
            }
        }

    }

    static class Node{
        int cnt;
        int y;
        int x;

        public Node(int cnt, int y, int x) {
            this.cnt = cnt;
            this.y = y;
            this.x = x;
        }
    }
}
