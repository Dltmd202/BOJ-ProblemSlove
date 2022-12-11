import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int INF = Integer.MAX_VALUE / 2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        int[][] graph = new int[V + 1][V + 1];
        for (int i = 0; i < V + 1; i++) {
            Arrays.fill(graph[i], INF);
            graph[i][i] = 0;
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int cur = Integer.parseInt(st.nextToken());
            int dest = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph[cur][dest] = cost;
        }


        for (int k = 1; k < V + 1; k++) {
            for (int i = 1; i < V + 1; i++) {
                for (int j = 1; j < V + 1; j++) {
                    graph[i][j]  = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        int res = INF;
        for (int i = 1; i < V + 1; i++) {
            for (int j = 1; j < V + 1; j++) {
                if(graph[i][j] >= INF || graph[j][i] >= INF || i == j)
                    continue;
                res = Math.min(res, graph[i][j] + graph[j][i]);
            }
        }

        System.out.println(res >= INF ? -1 : res);

    }

}