import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;
    private static int C;
    private static int[] X;
    private static int[] Y;
    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Node> q = new PriorityQueue<>(new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return (int) (o1.value - o2.value);
            }
        });

        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        X = new int[N];
        Y = new int[N];
        parent = new int[N + 1];

        for(int i = 0; i < N; i++){
            parent[i] = i;
        }

        for(int i = 0; i < N; i ++){
            st = new StringTokenizer(br.readLine());
            X[i] = Integer.parseInt(st.nextToken());
            Y[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < N - 1; i ++){
            for(int j = i + 1; j < N; j ++){
                long dist = (long) (Math.pow(X[i] - X[j], 2) + Math.pow(Y[i] - Y[j], 2));
                q.offer(new Node(i, j, dist));
            }
        }

        int dist = 0;
        int cnt = 0;
        while(!q.isEmpty()){
            Node now = q.poll();
            if(now.value < C) continue;

            int start = now.start, end = now.end;
            if(findParent(start) != findParent(end)){
                dist += now.value;
                unionParent(start, end);
                cnt ++;
            }
        }
        System.out.println(cnt == N - 1 ? dist: -1);
    }

    private static int findParent(int x){
        if(parent[x] != x) return findParent(parent[x]);
        return x;
    }

    private static void unionParent(int x, int y){
        x = findParent(x);
        y = findParent(y);
        if (x < y) parent[y] = x;
        else parent[x] = y;
    }

    public static class Node{
        private int start;
        private int end;
        private long value;

        public Node(int start, int end, long value) {
            this.start = start;
            this.end = end;
            this.value = value;
        }
    }
}
