import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[] s = br.readLine().toCharArray();

        int M = N / 2 + 1;
        char[] operator = new char[N / 2];
        long[] nums = new long[M];
        long[][] max = new long[M][M];
        long[][] min = new long[M][M];

        for (int i = 0; i < M - 1; i++) {
            Arrays.fill(max[i], Long.MIN_VALUE);
            Arrays.fill(min[i], Long.MAX_VALUE);
        }

        int oi = 0, ni = 0;
        for (int i = 0; i < N; i++) {
            if(i % 2 == 0) {
                max[ni][ni] = s[i] - '0';
                min[ni][ni] = s[i] - '0';
                nums[ni++] = s[i] - '0';
            }
            else
                operator[oi++] = s[i];
        }

        for (int i = 0; i < M - 1; i++) {
            max[i][i + 1] = calculate(nums[i], operator[i], nums[i + 1]);
            min[i][i + 1] = calculate(nums[i], operator[i], nums[i + 1]);
        }


        for (int interval = 2; interval < M; interval++) {
            int cnt = M - interval;
            for (int k = 0; k < cnt; k++) {
//                System.out.println(k + " " + (k + interval));
                for (int i = 0; i < interval; i++) {
                    long[] tmp = new long[4];
                    tmp[0] = calculate(max[k][k + i], operator[k + i], max[k + i + 1][k + interval]);
                    tmp[1] = calculate(max[k][k + i], operator[k + i], min[k + i + 1][k + interval]);
                    tmp[2] = calculate(min[k][k + i], operator[k + i], max[k + i + 1][k + interval]);
                    tmp[3] = calculate(min[k][k + i], operator[k + i], min[k + i + 1][k + interval]);

                    Arrays.sort(tmp);

                    max[k][k + interval] = Math.max(max[k][k + interval], tmp[3]);
                    min[k][k + interval] = Math.min(min[k][k + interval], tmp[0]);
//                    System.out.println("     " + k + " " + (k + i) + " " + (k + i + 1) + " " + (k + interval));
//                    System.out.println(dp[k][k + i] + " " + operator[k + i] + " " + dp[k + i + 1][k + interval]);
                }
            }
        }

//        for (int i = 0; i < M; i++) {
//            System.out.println(Arrays.toString(max[i]));
//        }

        System.out.println(max[0][M - 1]);
    }

    private static long calculate(long left, char operator, long right){
        if(operator == '+')
            return left + right;
        else if(operator == '-')
            return left - right;
        else
            return left * right;
    }
}