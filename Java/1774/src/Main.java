import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int M;
    private static int[] parent;
    private static int[] X;
    private static int[] Y;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Node> q = new PriorityQueue<>((o1, o2) -> Double.compare(o1.dist, o2.dist));
        ArrayList<Spot> spots = new ArrayList<>();
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        parent = new int[N + 1];
        for(int i = 0; i < N; i ++){
            parent[i] = i;
        }

        for(int i = 0; i < N; i ++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            spots.add(new Spot(x, y));

            for(int j = 0; j < i; j ++){
                double dist = Math.sqrt(
                        Math.pow(spots.get(i).x - spots.get(j).x, 2)
                                + Math.pow(spots.get(i).y - spots.get(j).y, 2)
                        );
                q.offer(new Node(i, j, dist));
            }
        }
        for(int i = 0; i < M; i ++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken()) - 1;
            int end = Integer.parseInt(st.nextToken()) - 1;
            unionParent(start, end);
        }

        double distance = 0.;
        while(!q.isEmpty()){
            Node now = q.poll();
            int start = now.start;
            int end = now.end;
            double dist = now.dist;

            if(findParent(start) != findParent(end)){
                unionParent(start, end);
                distance += dist;
            }
        }
        System.out.format("%.2f", distance);

    }

    public static int findParent(int x){
        if(parent[x] != x) return findParent(parent[x]);
        return x;
    }

    public static void unionParent(int x, int y){
        x = findParent(x);
        y = findParent(y);
        if (x > y) parent[x] = y;
        else parent[y] = x;
    }

    public static class Spot{
        private int x;
        private int y;

        public Spot(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static class Node{
        private int start;
        private int end;
        private double dist;

        public Node(int start, int end, double dist) {
            this.start = start;
            this.end = end;
            this.dist = dist;
        }
    }


}
