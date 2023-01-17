import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static Main.Ball[] balls;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        balls = new Ball[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            balls[i] = new Ball(
                    i,
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(balls);
        int[] result = new int[N];
        int[] colors = new int[N + 1];

        int sum = 0;
        for (int i = 0, j = 0; i < N; i++) {
            Ball a = balls[i];
            Ball b = balls[j];

            while (b.size < a.size){
                sum += b.size;

                colors[b.color] += b.size;

                b = balls[++j];
            }

            result[a.id] = sum - colors[a.color];
        }

        for (int i = 0; i < N; i++) {
            sb.append(result[i]).append("\n");
        }

        System.out.println(sb.toString().trim());
    }

    static class Ball implements Comparable<Ball>{
        int id;
        int color;
        int size;

        public Ball(int id, int color, int size) {
            this.id = id;
            this.color = color;
            this.size = size;
        }

        @Override
        public int compareTo(Ball ball){
            return size - ball.size;
        }
    }
}