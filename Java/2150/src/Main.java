import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static List<List<Integer>> graph;
    static List<List<Integer>> rGraph;
    static List<List<Integer>> SCC;
    static Stack<Integer> stack;
    static boolean[] visited;
    static int V;
    static int E;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        rGraph = new ArrayList<>();
        SCC = new ArrayList<>();

        for (int i = 0; i <= V; i++) {
            graph.add(new ArrayList<>());
            rGraph.add(new ArrayList<>());
            SCC.add(new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int now = Integer.parseInt(st.nextToken());
            int will = Integer.parseInt(st.nextToken());
            graph.get(now).add(will);
            rGraph.get(will).add(now);
        }
        visited = new boolean[V + 1];
        stack = new Stack<>();

        for (int i = 1; i < V; i++) {
            if(!visited[i]){
                dfs(i);
            }
        }

        Arrays.fill(visited, false);

        int groupNum = 0;

        while(!stack.isEmpty()){
            int start = stack.pop();

            if(visited[start]){
                continue;
            }

            redfs(start, groupNum++);
        }

        TreeMap<Integer, Integer> tm = new TreeMap<>();

        for (int i = 0; i < groupNum; i++) {
            Collections.sort(SCC.get(i));
            tm.put(SCC.get(i).get(0), i);
        }

        sb.append(groupNum).append("\n");
        tm.keySet().forEach((key) -> {
            int val = tm.get(key);
            for (int will : SCC.get(val)) {
                sb.append(will + " ");
            }
            sb.append("-1\n");
        });

        System.out.println(sb.toString());
    }

    static void dfs(int start){
        visited[start] = true;

        for (int will : graph.get(start)) {
            if(!visited[will]){
                dfs(will);
            }
        }
        stack.push(start);
    }

    static void redfs(int start, int groupNum){
        visited[start] = true;
        SCC.get(groupNum).add(start);

        for (int will : rGraph.get(start)) {
            if(!visited[will]){
                redfs(will, groupNum);
            }
        }
    }
}