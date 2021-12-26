import java.util.*;

public class Main {
    public static void main(String[] args) {
        int N, Q;
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        Q = sc.nextInt();
        List<int[]>[] graph = new ArrayList[N + 1];

        for(int i = 1; i <= N; i ++)
            graph[i] = new ArrayList<>();

        for(int i = 1; i < N; i ++){
            int p = sc.nextInt();
            int q = sc.nextInt();
            int r = sc.nextInt();
            graph[p].add(new int[] {q, r});
            graph[q].add(new int[] {p, r});
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < Q; i ++){
            int k = sc.nextInt();
            int v = sc.nextInt();

            boolean[] visited = new boolean[N + 1];
            visited[v] = true;
            Queue<Integer> que = new LinkedList<>();
            que.add(v);

            int res = 0;
            while(!que.isEmpty()){
                int now = que.poll();
                for(int[] will: graph[now]){
                    if(!visited[will[0]] && will[1] >= k){
                        que.add(will[0]);
                        visited[will[0]] = true;
                        res += 1;
                    }
                }
            }
            sb.append(res).append('\n');
        }
        System.out.println(sb.toString());

    }
}
