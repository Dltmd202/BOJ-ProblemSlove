import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[][] graph;
    private static boolean[] visited;
    private static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        graph = new int[N + 1][N + 1];
        visited = new boolean[N + 1];
        for(int i = 1; i <= N; i ++){
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j <= N; j ++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ArrayList<Integer> travel = new ArrayList<>();
        travel.add(1);
        travel(travel, 1, graph[1][1]);
        System.out.println(answer);
    }

    public static void travel(ArrayList<Integer> traveled, int now, int cost){
        if(traveled.size() == N + 1 && traveled.get(N) == 1){
            answer = Math.min(answer, cost);
        }

        for(int will = 1; will <= N; will ++){
            if(graph[now][will] != 0 && !visited[will]){
                visited[will] = true;
                traveled.add(will);

                travel(traveled, will, cost + graph[now][will]);

                visited[will] = false;
                traveled.remove(traveled.size() - 1);
            }
        }
    }
}
