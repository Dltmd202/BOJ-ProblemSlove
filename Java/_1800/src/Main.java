import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int P;
    static int K;
    static List<Node>[] map;
    static int[] distance;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        map = new ArrayList[N + 1];
        distance = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            map[i] = new ArrayList<>();
        }

        int max = 0;

        for (int i = 0; i < P; i++) {
            st = new StringTokenizer(br.readLine());

            int now = Integer.parseInt(st.nextToken());
            int will = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            map[now].add(new Node(will, dist));
            map[will].add(new Node(now, dist));

            max = Math.max(max, dist);
        }

        int start = 0;
        int answer = Integer.MIN_VALUE;

        while (start <= max){
            int mid = (start + max) / 2;

            if(dijkstra(mid)){
                answer = mid;
                max = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        if(answer == Integer.MIN_VALUE){
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }

    private static boolean dijkstra(int val){
        Queue<Node> pq = new PriorityQueue<>();

        Arrays.fill(distance, Integer.MAX_VALUE);

        distance[1] = 0;

        pq.offer(new Node(1, 0));

        while (!pq.isEmpty()){
            Node cur = pq.poll();

            int now = cur.id;
            int cost = cur.dist;

            if(distance[now] < cost) continue;

            for (Node nextNode : map[now]) {
                int next = nextNode.id;
                int nc = cost;

                if(nextNode.dist > val) nc++;

                if(nc < distance[next]){
                    distance[next] = nc;
                    pq.offer(new Node(next, nc));
                }
            }

        }

        return distance[N] <= K;
    }

    static class Node implements Comparable<Node>{
        int id;
        int dist;

        public Node(int id, int dist) {
            this.id = id;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node o) {
            return this.dist - o.dist;
        }
    }
}