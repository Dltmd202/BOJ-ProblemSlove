import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static Work[] works;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        works = new Work[N + 1];
        int[] dp = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            works[i] = new Work(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }

        for (int i = 1; i <= N; i++) {
            int next = i + works[i].t - 1;

            if(next <= N){
                dp[next] = Math.max(dp[i - 1] + works[i].p, dp[next]);
            }
            dp[i] = Math.max(dp[i], dp[i - 1]);
        }

        System.out.println(dp[N]);
    }

    static class Work{
        int t;
        int p;

        public Work(int t, int p) {
            this.t = t;
            this.p = p;
        }
    }
}