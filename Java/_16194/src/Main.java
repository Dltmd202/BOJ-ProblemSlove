import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] data = new int[N + 1];
        int[] dp = new int[N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            data[i] = Integer.parseInt(st.nextToken());
            dp[i] = data[i];
        }

        for (int i = 2; i <= N; i++) {
            int min = dp[i];
            for (int j = i - 1; j >= i / 2 ; j--) {
                min = Math.min(min, dp[j] + dp[i - j]);
            }
            dp[i] = min;
        }

        System.out.println(dp[N]);
    }
}
