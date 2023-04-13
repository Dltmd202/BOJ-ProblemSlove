import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] data = new int[N];
        int[][] dp = new int[10_001][4];



        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(br.readLine());
        }

        dp[1][0] = 1;
        dp[1][1] = 0;
        dp[1][2] = 0;

        dp[2][0] = 2;
        dp[2][1] = 1;
        dp[2][2] = 0;

        dp[3][0] = 3;
        dp[3][1] = 1;
        dp[3][2] = 1;

        dp[4][0] = 4;
        dp[4][1] = 1;
        dp[4][2] = 0;



        for (int i = 5; i <= 10_000; i++) {
            dp[i][2] = dp[i - 3][2];
            dp[i][1] = dp[i - 2][1] + dp[i][2];
            dp[i][0] = dp[i - 1][0] + dp[i][1];
        }

        for (int i = 0; i < N; i++) {
            System.out.println(dp[data[i]][0]);
        }

    }
}
