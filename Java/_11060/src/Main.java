import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] data = new int[N];
        int[] dp = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        dp[N - 1] = 0;
        for (int i = N - 2; i >= 0 ; i--) {
            if(i + data[i] >= N) dp[i] = 1;
            else{
                int min = Integer.MAX_VALUE;
                for (int j = 1; j <= data[i] && i + j < N; j++) {
                    if(dp[i + j] == Integer.MAX_VALUE) continue;
                    min = Math.min(min, 1 + dp[i + j]);
                }
                dp[i] = min;
            }
        }

        System.out.println(dp[0] == Integer.MAX_VALUE ? -1 : dp[0]);

    }
}
