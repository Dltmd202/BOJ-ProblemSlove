import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Matrix[] matrices = new Matrix[N + 1];
        int[][] dp = new int[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            matrices[i] = new Matrix(r, c);
        }

        for (int i = 1; i < N; i++) {
            dp[i][i + 1] = matrices[i].r * matrices[i].c * matrices[i + 1].c;
        }

        for (int i = 3; i <= N; i++) {
            for (int left = i; left <= N; left++) {
                int right = left - i + 1;
                int section = i - 1;
                int optimized = Integer.MAX_VALUE;


                for (int k = 0; k < section; k++) {
                    int rightStart = right;
                    int rightEnd = right + k;
                    int leftStart = rightEnd + 1;
                    int leftEnd = left;
                    Matrix rightMatrix = getMutipliedMatrix(matrices, rightStart, rightEnd);
                    Matrix leftMatrix = getMutipliedMatrix(matrices, leftStart, leftEnd);
                    optimized = Math.min(
                            optimized,
                            dp[rightStart][rightEnd] + dp[leftStart][leftEnd] +
                                    rightMatrix.r * rightMatrix.c * leftMatrix.c
                    );
                }
                dp[right][left] = optimized;
            }
        }

        System.out.println(dp[1][N]);
    }

    public static Matrix getMutipliedMatrix(Matrix[] matrices, int right, int left){
        return new Matrix(matrices[right].r, matrices[left].c);
    }

    static class Matrix{
        int r;
        int c;

        public Matrix(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}