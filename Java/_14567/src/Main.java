
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private static int N;
    private static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        List<Integer>[] graph = new List[N + 1];
        Queue<Integer> q = new ArrayDeque<>();
        int[] inDegree = new int[N + 1];
        int[] dp = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int pre = Integer.parseInt(st.nextToken());
            int post = Integer.parseInt(st.nextToken());

            graph[pre].add(post);
            inDegree[post]++;
        }


        int semester = 1;
        for (int i = 1; i <= N; i++) {
            if(inDegree[i] == 0){
                q.add(i);
                dp[i] = semester;
            }
        }

        while (!q.isEmpty()){
            semester++;

            int cnt = q.size();
            for (int i = 0; i < cnt; i++) {
                Integer cur = q.poll();

                for (Integer next : graph[cur]) {
                    inDegree[next]--;

                    if(inDegree[next] == 0){
                        dp[next] = semester;
                        q.offer(next);
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(dp[i]).append(" ");
        }

        System.out.println(sb.toString().trim());


    }

    static class Node{

    }
}
