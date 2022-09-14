import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int seq = 1;

        List<Edge>[] edges = new List[N + 1];

        for (int i = 0; i <= N; i++) {
            edges[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int now = Integer.parseInt(st.nextToken());
            int will = Integer.parseInt(st.nextToken());

            edges[now].add(new Edge(now, will));
            edges[will].add(new Edge(will, now));
        }

        Arrays.stream(edges)
                .forEach(l -> l.sort(Edge::compareTo));

        Queue<Integer> q = new ArrayDeque<>();
        int[] visited = new int[N + 1];
        visited[R] = seq++;
        q.offer(R);

        while (!q.isEmpty()){
            int now = q.poll();

            for(Edge next: edges[now]){
                if(visited[next.will] == 0){
                    visited[next.will] = seq++;
                    q.offer(next.will);
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.println(visited[i]);
        }
    }

    static class Edge implements Comparable<Edge>{
        int now;
        int will;

        public Edge(int now, int will) {
            this.now = now;
            this.will = will;
        }

        @Override
        public int compareTo(Edge o) {
            return will - o.will;
        }
    }
}