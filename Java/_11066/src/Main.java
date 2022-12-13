import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-->0){
            int K = Integer.parseInt(br.readLine());
            int[] files = new int[K + 1];
            int[] sumWindow = new int[K + 1];
            int[][] dp = new int[K + 1][K + 1];
            sumWindow[0] = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= K; i++) {
                files[i] = Integer.parseInt(st.nextToken());
                sumWindow[i] = files[i] + sumWindow[i - 1];
            }

            for (int i = 1; i < K; i++) {
                dp[i][i + 1] = files[i] + files[i + 1];
            }

            for (int i = 0; i < K - 2; i++) {
                for (int searchingStartIdx = 1; searchingStartIdx < K - i - 1; searchingStartIdx++) {
                    int possibleCombinationCount = i + 3;
                    int searchingEndIdx = searchingStartIdx + possibleCombinationCount - 1;

                    int mergeCost = rangeSum(sumWindow, searchingStartIdx, searchingEndIdx);
                    int leastPartCost = Integer.MAX_VALUE;

                    for (int k = 0; k < possibleCombinationCount - 1; k++) {
                        leastPartCost = Math.min(
                                leastPartCost,
                                dp[searchingStartIdx][searchingStartIdx + k] + dp[searchingStartIdx + k + 1][searchingEndIdx]
                        );
                    }

                    mergeCost += leastPartCost;
                    dp[searchingStartIdx][searchingEndIdx] = mergeCost;
                }
            }

            System.out.println(dp[1][K]);
        }
    }

    public static int rangeSum(int[] sw, int s, int e){
        return sw[e] - sw[s - 1];
    }
}