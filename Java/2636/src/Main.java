import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int[][] graph;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int n, m;

    public static class Node{
        int y;
        int x;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        bfs();
    }

    public static void bfs(){
        Queue<Node> q = new LinkedList<>();
        Queue<Node> nextQ = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        int leave = 0;
        int turn = 0;
        q.add(new Node(0, 0));
        visited[0][0] = true;

        searchHole(q, nextQ, visited);


        Queue<Node> tmp = q;
        q = nextQ;
        nextQ = tmp;

        
        while (!q.isEmpty()){

            turn++;

            int leaveTmp = 0;
            while(!q.isEmpty()){
                Node now = q.poll();
                for (int i = 0; i < 4; i++) {
                    int ny = now.y + dy[i];
                    int nx = now.x + dx[i];

                    if(0 <= ny && ny < n && 0 <= nx && nx < m){
                        if(graph[ny][nx] == 1 && !visited[ny][nx]){
                            nextQ.offer(new Node(ny, nx));
                            graph[ny][nx] = 0;
                            visited[ny][nx] = true;
                            leaveTmp++;
                        } else if(graph[ny][nx] == 0 && !visited[ny][nx]){
                            Queue<Node> holeQ = new LinkedList<>();
                            Node newHole = new Node(ny, nx);
                            holeQ.offer(newHole);
                            nextQ.offer(newHole);
                            searchHole(holeQ, q, visited);
                        }
                    }
                }
            }
            if(leaveTmp == 0){
                break;
            } else {
                tmp = q;
                q = nextQ;
                nextQ = tmp;
                leave = leaveTmp;
            }
        }
        System.out.println(turn - 1);
        System.out.println(leave);
    }

    private static void searchHole(Queue<Node> q, Queue<Node> nextQ, boolean[][] visited) {
        while (!q.isEmpty()){
            Node now = q.poll();

            for (int i = 0; i < 4; i++) {
                int ny = now.y + dy[i];
                int nx = now.x + dx[i];
                if(0 <= ny && ny < n && 0 <= nx && nx < m) {
                    if (graph[ny][nx] == 0 && !visited[ny][nx]) {
                        Node nNode = new Node(ny, nx);
                        q.add(nNode);
                        nextQ.add(nNode);
                        visited[ny][nx] = true;
                    }
                }
            }
        }
    }
}
