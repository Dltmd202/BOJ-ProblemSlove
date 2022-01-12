import java.util.Scanner;

public class Main {
    private static int N;
    private static int[] data;
    private static int[] dp;
    private static int answer = 1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        data = new int[N];
        dp = new int[N];
        for(int i = 0; i < N; i++){
            data[i] = sc.nextInt();
        }
        dp[0] = 1;

        for(int i = 1; i < N; i ++){
            dp[i] = 1;
            for(int j = 0; j < i; j ++){
                if(data[j] > data[i]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    answer = Math.max(answer, dp[i]);
                }
            }
        }
        System.out.println(answer);

    }
}
