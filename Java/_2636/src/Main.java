import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {0, 0, 1, -1};
    static int N;
    static int M;
    static int total = 0;
    static int[] dy = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                total += map[i][j];
            }
        }

        int time = 0;
        int cnt = 0;

        while (total > 0){
            cnt = bfs(map);
            time++;
            total -= cnt;
        }

        System.out.println(time);
        System.out.println(cnt);


    }

    public static int bfs(int[][] map){
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][M];
        q.offer(new int[]{0, 0});
        int cnt = 0;

        while (!q.isEmpty()){
            int[] cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int ny = cur[0] + dy[i];
                int nx = cur[1] + dx[i];

                if(0 <= ny && ny < N && 0 <= nx && nx <M && !visited[ny][nx]){
                    if(map[ny][nx] == 1) {
                        map[ny][nx] = 0;
                        cnt++;
                    }
                    else {
                        q.offer(new int[]{ny, nx});
                    }
                    visited[ny][nx] = true;
                }
            }
        }

        return cnt;
    }
}