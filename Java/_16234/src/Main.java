import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int N;
    static int L;
    static int R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 0;
        while (true){
            boolean[][] visited = new boolean[N][N];
            List<List<int[]>> unions = new ArrayList<>();
            List<Integer> populations = new ArrayList<>();
            int id = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if(!visited[i][j]){
                        unions.add(new ArrayList<>());
                        populations.add(bfs(map, visited, unions.get(id++), i, j));
                    }
                }
            }

            if(N * N == unions.size()) break;
            else {
                for (int i = 0; i < unions.size(); i++) {
                    List<int[]> union = unions.get(i);
                    int newPop = populations.get(i) / union.size();

                    for(int[] cur : union){
                        map[cur[0]][cur[1]] = newPop;
                    }
                }
            }
            time++;
        }
        System.out.println(time);
    }

    public static int bfs(int[][] map, boolean[][] visited, List<int[]> union, int y, int x){
        Queue<int[]> q = new ArrayDeque<>();
        visited[y][x] = true;
        union.add(new int[]{y, x});
        q.offer(new int[]{y, x});

        int population = map[y][x];

        while (!q.isEmpty()){
            int[] cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int ny = cur[0] + dy[i];
                int nx = cur[1] + dx[i];

                if(0 > ny || ny >= N || 0 > nx || nx >= N) continue;
                if(visited[ny][nx]) continue;

                int diff = Math.abs(map[cur[0]][cur[1]] - map[ny][nx]);
                if(diff < L || diff > R) continue;

                union.add(new int[]{ny, nx});
                q.offer(new int[]{ny, nx});
                visited[ny][nx] = true;
                population += map[ny][nx];
            }
        }

        return population;
    }
}