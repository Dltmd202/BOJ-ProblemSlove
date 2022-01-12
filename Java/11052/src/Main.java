import java.util.Scanner;

public class Main {
    private static int N;
    private static int[] cards;
    private static int[] dp;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        cards = new int[N + 1];
        dp = new int[N + 1];
        for(int i = 1; i <= N; i ++){
            cards[i] = sc.nextInt();
        }
        dp[1] = cards[1];

        for(int i = 2; i <= N; i ++){
            int cost = cards[i];
            for(int j = 1; j <= i / 2; j ++){
                cost = Math.max(cost, dp[j] + dp[i - j]);
            }
            dp[i] = cost;
        }
        System.out.println(dp[dp.length - 1]);
    }
}
