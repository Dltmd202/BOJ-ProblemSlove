import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int K;
    private static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());



        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graph = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        boolean[] visited = new boolean[N];
        visited[K] = true;
        System.out.println(search(visited, K, 0, N - 1));
    }

    public static int search(boolean[] visited, int cur, int cost, int level){
        if(level == 0){
            return cost;
        }

        int ret = Integer.MAX_VALUE;
        for (int next = 0; next < N; next++) {
            if(visited[next]) continue;

            visited[next] = true;
            ret = Math.min(ret, search(visited, next, cost + graph[cur][next], level - 1));
            visited[next] = false;
        }

        return ret;
    }

}