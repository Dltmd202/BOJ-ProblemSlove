import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int[][] graph;
    private static boolean[] visited;
    private static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        search(new ArrayList<>(), 0);
        System.out.println(res);
    }

    public static void search(List<Integer> team, int idx){
        if(team.size() > 0 && team.size() < N) {
            res = Math.min(res, getAbilityDiff(team));
        }

        for (int i = idx; i < N; i++) {
            team.add(i);

            search(team, i + 1);

            team.remove(team.size() - 1);
        }
    }
    
    public static int getAbilityDiff(List<Integer> team){

        Arrays.fill(visited, false);

        int startScore = 0;
        for (int i = 0; i < team.size() - 1; i++) {
            int a = team.get(i);
            for (int j = i + 1; j < team.size(); j++) {
                int b = team.get(j);
                startScore += graph[a][b];
                startScore += graph[b][a];
            }
        }

        for (int unit : team) {
            visited[unit] = true;
        }

        ArrayList<Integer> link = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            if(!visited[i]) {
                link.add(i);
            }
        }

        int linkScore = 0;
        for (int i = 0; i < link.size() - 1; i++) {
            int a = link.get(i);
            for (int j = i + 1; j < link.size(); j++) {
                int b = link.get(j);
                linkScore += (graph[a][b] + graph[b][a]);
            }
        }
        return Math.abs(linkScore - startScore);
    }
}