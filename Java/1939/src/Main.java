import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static List<Bridge>[] graph;
    static int factory1;
    static int factory2;
    static int answer;

    static class Bridge{
        int depart;
        int arrive;
        int limit;

        public Bridge(int depart, int arrive, int limit) {
            this.depart = depart;
            this.arrive = arrive;
            this.limit = limit;
        }
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 0; i < graph.length; i++) {
            graph[i] = new ArrayList<>();
        }

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            int limit = Integer.parseInt(st.nextToken());

            graph[node2].add(new Bridge(node2, node1, limit));
            graph[node1].add(new Bridge(node1, node2, limit));
        }
        st = new StringTokenizer(br.readLine());
        factory1 = Integer.parseInt(st.nextToken());
        factory2 = Integer.parseInt(st.nextToken());

        parametricSearch();
        System.out.println(answer);
    }

    static boolean bfs(int limit){
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[N + 1];
        visited[factory1] = true;
        q.add(factory1);

        while(!q.isEmpty()){
            int cur = q.poll();

            if(cur == factory2){
                answer = Math.max(answer, limit);
                return true;
            }

            for (Bridge bridge : graph[cur]) {
                if(!visited[bridge.arrive] && bridge.limit >= limit){
                    q.add(bridge.arrive);
                    visited[bridge.arrive] = true;
                }
            }
        }
        return false;
    }

    static void parametricSearch(){
        int left = 1, right = 1_000_000_000;

        while(left <= right){
            int mid = (left + right) / 2;

            if(bfs(mid)) left = mid + 1;
            else right = mid - 1;
        }
    }

}
