import java.io.*;
import java.util.*;

public class Main {

    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = {0, 1, 0, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[][] graph = new char[N][M];
        boolean[][][][] visited = new boolean[N][M][N][M];
        int[] hole = null;
        Situation situation = new Situation(0, 0, 0, 0, 1);


        for (int i = 0; i < N; i++) {

            graph[i] = br.readLine().toCharArray();

            for (int j = 0; j < M; j++) {
                if(graph[i][j] == 'O'){
                    hole = new int[] {i, j};
                } else if(graph[i][j] == 'B'){
                    situation.by = i;
                    situation.bx = j;
                } else if(graph[i][j] == 'R'){
                    situation.ry = i;
                    situation.rx = j;
                }
            }
        }

        System.out.println(bfs(graph, visited, hole, situation));
    }

    public static int bfs(char[][] graph, boolean[][][][] visited, int[] hole, Situation init){
        int N = graph.length;
        int M = graph[0].length;

        Queue<Situation> q = new ArrayDeque<>();
        q.add(init);
        visited[init.ry][init.rx][init.by][init.bx] = true;

        while (!q.isEmpty()){
            Situation cur = q.poll();

            if(cur.cnt > 10) return -1;

            for (int i = 0; i < 4; i++) {
                int nry = cur.ry;
                int nrx = cur.rx;
                int nby = cur.by;
                int nbx = cur.bx;

                boolean isRedHole = false;
                boolean isBlueHole = false;

                while(graph[nry + dy[i]][nrx + dx[i]] != '#'){
                    nry += dy[i];
                    nrx += dx[i];

                    if(nry == hole[0] && nrx == hole[1]){
                        isRedHole = true;
                        break;
                    }
                }

                while (graph[nby + dy[i]][nbx + dx[i]] != '#') {
                    nby += dy[i];
                    nbx += dx[i];

                    if(nby == hole[0] && nbx == hole[1]){
                        isBlueHole = true;
                        break;
                    }
                }

                if(isBlueHole)
                    continue;

                if(isRedHole)
                    return cur.cnt;

                if(nry == nby && nrx == nbx){
                    if(i == 0){
                        if(cur.ry > cur.by) nry -= dy[i];
                        else nby -= dy[i];
                    } else if(i == 1){
                        if(cur.rx < cur.bx) nrx -= dx[i];
                        else nbx -= dx[i];
                    } else if(i == 2){
                        if(cur.ry < cur.by) nry -= dy[i];
                        else nby -= dy[i];
                    } else if(i == 3){
                        if(cur.rx > cur.bx) nrx -= dx[i];
                        else nbx -= dx[i];
                    }
                }

                if(!visited[nry][nrx][nby][nbx]){
                    visited[nry][nrx][nby][nbx] = true;
                    q.offer(new Situation(nry, nrx, nby, nbx, cur.cnt + 1));
                }
            }
        }

        return -1;
    }

    static class Situation{
        int ry;
        int rx;
        int by;
        int bx;
        int cnt;

        public Situation(int ry, int rx, int by, int bx, int cnt) {
            this.ry = ry;
            this.rx = rx;
            this.by = by;
            this.bx = bx;
            this.cnt = cnt;
        }
    }
}
