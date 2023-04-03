import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private static int V;
    private static int E;
    private static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        List<Node>[] graph = new List[V + 1];

        for (int i = 0; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }

        int[] distance = new int[V + 1];

        for (int i = 0; i <= V; i++) {
            distance[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new Node(u, v, w));
        }

        Queue<Node> q = new PriorityQueue<>();
        q.offer(new Node(K, K, 0));
        distance[K] = 0;

        while (!q.isEmpty()){
            Node cur = q.poll();


            if(distance[cur.v] > cur.w) continue;

            for (Node node : graph[cur.v]) {
                int nw = cur.w + node.w;

                if(nw < distance[node.v]){
                    distance[node.v] = nw;
                    q.offer(new Node(cur.v, node.v, nw));
                }

            }
        }


        System.out.println(
                Arrays.stream(distance, 1, distance.length)
                        .mapToObj(d -> d < Integer.MAX_VALUE ? String.valueOf(d) : "INF")
                        .collect(Collectors.joining("\n"))
        );
    }

    public static class Node implements Comparable<Node>{
        private int u;
        private int v;
        private int w;

        public Node(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }

        @Override
        public int compareTo(Node o) {
            return this.w - o.w;
        }
    }
}