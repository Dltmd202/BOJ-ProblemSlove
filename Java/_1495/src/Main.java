import java.util.*;
import java.io.*;

public class Main {

    private static int N;
    private static int S;
    private static int M;
    private static int[] volumes;
    private static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        volumes = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            volumes[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[M + 1][N];
        for (int[] d : dp) {
            Arrays.fill(d, -2);
        }

        System.out.println(search(S, 0));


    }

    public static int search(int sum, int idx){
        if(sum > M || sum < 0) return -1;

        if(idx == N){
            return sum;
        }

        if(dp[sum][idx] != -2){
            return dp[sum][idx];
        }

        int left = search(sum + volumes[idx], idx + 1);
        int right = search(sum - volumes[idx], idx + 1);
        int max = Math.max(left, right);
        dp[sum][idx] = Math.max(dp[sum][idx], max);

        return dp[sum][idx];

    }
}
