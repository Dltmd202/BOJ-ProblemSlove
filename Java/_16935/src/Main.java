import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

    private static int N;
    private static int M;
    private static int R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Command[] commands = new Command[]{
                null,
                Main::invertVerticalSide,
                Main::invertHorizontalSide,
                Main::rotateClockwise,
                Main::rotateCounterClockwise,
                Main::divideRotateClockwise,
                Main::divideRotateCounterClockwise
        };

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        int[][] matrix = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < R; i++) {
            int order = Integer.parseInt(st.nextToken());
            matrix = commands[order].rotate(matrix);
        }

        for (int i = 0; i < matrix.length; i++) {
            sb.append(Arrays.stream(matrix[i]).mapToObj(String::valueOf).collect(Collectors.joining(" ")))
                    .append("\n");
        }

        System.out.println(sb.toString().trim());
    }

    interface Command {
        int[][] rotate(int[][] matrix);
    }

    public static int[][] invertVerticalSide(int[][] matrix){
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] newMatrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                newMatrix[i][j] = matrix[n - i - 1][j];
            }
        }

        return newMatrix;
    }

    public static int[][] invertHorizontalSide(int[][] matrix){
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] newMatrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                newMatrix[i][j] = matrix[i][m - j - 1];
            }
        }

        return newMatrix;
    }

    public static int[][] rotateClockwise(int[][] matrix){
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] newMatrix = new int[m][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                newMatrix[j][n - i - 1] = matrix[i][j];
            }
        }

        return newMatrix;
    }

    public static int[][] rotateCounterClockwise(int[][] matrix){
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] newMatrix = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                newMatrix[i][j] = matrix[j][m - 1 - i];
            }
        }

        return newMatrix;
    }

    public static int[][] divideRotateCounterClockwise(int[][] matrix){
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] newMatrix = new int[n][m];

        for(int i = 0; i < n / 2; i++) {
            System.arraycopy(matrix[i], 0, newMatrix[i + n / 2], 0, m / 2);
        }

        for(int i = n / 2; i < n; i++) {
            System.arraycopy(matrix[i], 0, newMatrix[i], 0 + m / 2, m / 2);
        }

        for(int i = n / 2; i < n; i++) {
            System.arraycopy(matrix[i], m / 2, newMatrix[i - n / 2], m / 2, m - m / 2);
        }

        for(int i = 0; i < n / 2; i++) {
            System.arraycopy(matrix[i], m / 2, newMatrix[i], m / 2 - m / 2, m - m / 2);
        }

        return newMatrix;
    }

    public static int[][] divideRotateClockwise(int[][] matrix){
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] newMatrix = new int[n][m];

        for(int i = 0; i < n / 2; i++) {
            System.arraycopy(matrix[i], 0, newMatrix[i], 0 + m / 2, m / 2);
        }

        for(int i = 0; i < n / 2; i++) {
            System.arraycopy(matrix[i], m / 2, newMatrix[i + n / 2], m / 2, m - m / 2);
        }

        for(int i = n / 2; i < n; i++) {
            System.arraycopy(matrix[i], m / 2, newMatrix[i], m / 2 - m / 2, m - m / 2);
        }

        for(int i = n / 2; i < n; i++) {
            System.arraycopy(matrix[i], 0, newMatrix[i - n / 2], 0, m / 2);
        }

        return newMatrix;
    }

}
