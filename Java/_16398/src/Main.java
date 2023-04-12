import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int[] parents = new int[N + 1];
        for (int i = 0; i < N; i++) {
            parents[i] = i;
        }

        List<Edge> edges = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int cost = Integer.parseInt(st.nextToken());
                if(i == j) continue;
                edges.add(new Edge(i, j, cost));
            }
        }

        edges.sort((a, b) -> a.cost - b.cost);


        long cost = 0;
        for (int i = 0; i < edges.size(); i++) {
            Edge edge = edges.get(i);

            if(find(parents, edge.a) != find(parents, edge.b)){
                union(parents, edge.a, edge.b);
                cost += edge.cost;
            }
        }

        System.out.println(cost);
    }


    public static int find(int[] parents, int x){
        if(parents[x] != x)
            parents[x] = find(parents, parents[x]);
        return parents[x];
    }

    public static void union(int[] parents, int a, int b){
        int A = find(parents, a);
        int B = find(parents, b);

        if(A > B){
            parents[A] = B;
        } else {
            parents[B] = A;
        }
    }


    static class Edge{
        int a;
        int b;
        int cost;

        public Edge(int a, int b, int cost) {
            this.a = a;
            this.b = b;
            this.cost = cost;
        }

        public String toString(){
            return "( " + a + ", "  + b + ", " + cost + " )";
        }
    }
}
