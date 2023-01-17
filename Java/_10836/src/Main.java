import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    private static int M;
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        int[] grad = new int[2 * M - 1];
        int[][] map = new int[M][M];

        Arrays.fill(grad, 1);

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int idx = 0;
            for (int j = 0; j < 3; j++) {
                int cnt = Integer.parseInt(st.nextToken());
                for (int k = 0; k < cnt; k++) {
                    grad[idx++] += j;
                }
            }
        }

        int idx = 0;
        for (int i = M - 1; i >= 0; i--) {
            map[i][0] = grad[idx++];
        }

        for (int i = 1; i < M; i++) {
            map[0][i] = grad[idx++];
        }

        for (int i = 1; i < M; i++) {
            for (int j = 1; j < M; j++) {
                map[i][j] = Math.max(map[i - 1][j], Math.max(map[i - 1][j - 1], map[i][j - 1]));
            }
        }

        for (int i = 0; i < M; i++) {
            sb.append(Arrays.stream(map[i]).mapToObj(String::valueOf).collect(Collectors.joining(" ")))
                    .append('\n');
        }

        System.out.println(sb.toString().trim());

   }
}