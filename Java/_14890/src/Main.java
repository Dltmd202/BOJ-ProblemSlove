import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int L;
    private static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        graph = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            if(calRow(i)) cnt++;
            if(calCol(i)) cnt++;
        }

        System.out.println(cnt);
    }

    public static boolean calRow(int r){
        boolean[] isInclinde = new boolean[N];

        for (int i = 0; i < N - 1; i++) {
            int diff = graph[r][i + 1] - graph[r][i];

            if(diff > 1 || diff < -1) return false;
            else if(diff == 1){
                for (int j = 0; j < L; j++) {
                    if(i - j < 0 || isInclinde[i - j]) return false;
                    if(graph[r][i] != graph[r][i - j]) return false;
                    isInclinde[i - j] = true;
                }
            }
            else if(diff == -1){
                for (int j = 1; j <= L; j++) {
                    if(i + j >= N || isInclinde[i + j]) return false;
                    if(graph[r][i] - 1 != graph[r][i + j]) return false;
                    isInclinde[i + j] = true;
                }
            }
        }
        return true;
    }

    public static boolean calCol(int col){
        boolean[] isInclude = new boolean[N + 1];

        for (int i = 0; i < N - 1; i++) {
            int diff = graph[i + 1][col] - graph[i][col];

            if(Math.abs(diff) > 1) return false;
            else if(diff == 1){
                for (int j = 0; j < L; j++) {
                    if(i - j < 0 || isInclude[i - j]) return false;
                    if(graph[i][col] != graph[i - j][col]) return false;
                    isInclude[i - j] = true;
                }
            }
            else if(diff == -1){
                for (int j = 1; j <= L; j++) {
                    if(i + j >= N || isInclude[i + j]) return false;
                    if(graph[i][col] - 1 != graph[i + j][col]) return false;
                    isInclude[i + j] = true;
                }
            }
        }
        return true;
    }
}
