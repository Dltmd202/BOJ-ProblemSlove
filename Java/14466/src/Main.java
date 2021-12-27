import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;
    private static int[] dx = {0, 0, 1, -1};
    private static int[] dy = {1, -1, 0, 0};

    static class Node{
        private int x;
        private int y;

        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            Node node = (Node) obj;
            return this.x == node.x && this.y == node.y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int answer = 0;

        int[][] map = new int[N + 1][N + 1];
        ArrayList<Node>[][] bridges = new ArrayList[N + 1][N + 1];

        for(int i = 1; i < N + 1; i ++){
            for(int j = 1; j < N + 1; j ++){
                bridges[i][j] = new ArrayList<>();
            }
        }

        for(int i = 0; i < R; i ++){
            st = new StringTokenizer(br.readLine());

            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());

            bridges[r1][c1].add(new Node(r2, c2));
            bridges[r2][c2].add(new Node(r1, c1));
        }

        List<Node> cows = new ArrayList<>();
        for(int i = 0; i < K; i ++){
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            cows.add(new Node(x, y));
            map[x][y] = 1;
        }

        for(int t = 0; t < K; t ++){
            Node cow = cows.get(t);

            boolean[][] visited = new boolean[N + 1][N + 1];
            boolean[][] cowContacted = new boolean[K][K];
            Queue<Node> q = new LinkedList<>();
            q.offer(cow);

            while(!q.isEmpty()){
                Node now = q.poll();

                if(map[now.x][now.y] == 1){
                    for(int j = t + 1; j < K; j++){
                        Node next = cows.get(j);
                        if(next.x == now.x && next.y == now.y) {
                            cowContacted[t][j] = true;
                            break;
                        }
                    }
                }

                for(int i = 0; i < 4; i ++){
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];

                    if(0 < nx && nx <= N && 0 < ny && ny <= N){
                        if(!visited[nx][ny]){
                            if(!bridges[now.x][now.y].contains(new Node(nx, ny))){
                                visited[nx][ny] = true;
                                q.offer(new Node(nx, ny));
                            }
                        }
                    }
                }
            }
            for(int i = t + 1; i < K; i ++){
                if(!cowContacted[t][i]){
                    answer ++;
                }
            }
        }
        System.out.println(answer);
    }
}
