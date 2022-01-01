import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int M;
    private static int H;
    private static int[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        graph = new int[H + 1][N + 1];

        for(int i = 0; i < M; i ++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[a][b + 1] = -1;
        }


        for(int i = 0; i <= 3; i ++){
            if(dfs(i)){
                System.out.println(i);
                return;
            }
        }
        System.out.println(-1);
    }

    private static void printGraph(){
        for(int i = 1; i <= H; i ++){
            for(int j = 1; j <= N; j ++){
                System.out.format("%3d", graph[i][j]);
            }
            System.out.println();
        }
        System.out.println("\n");
    }

    private static boolean dfs(int cnt){
//        printGraph();
        if(isFinished()) return true;
        if(cnt == 0) return false;
        boolean res = false;
        for(int i = 1; i <= H; i ++){
            for(int j = 1; j < N; j ++){
                if(graph[i][j] == 0 && graph[i][j + 1] == 0){
                    graph[i][j] = 1;
                    graph[i][j + 1] = -1;

                    if(dfs(cnt - 1)) return true;

                    graph[i][j] = 0;
                    graph[i][j + 1] = 0;
                }
            }
        }
        return res;
    }

    private static boolean isFinished(){
        for(int i = 1; i <= N; i ++){
            int x = i;
            for(int y = 1; y <= H; y ++){
                x += graph[y][x];
            }
            if(x != i) return false;
        }
        return true;
    }
}
