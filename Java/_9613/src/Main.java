import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        while (T-->0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int[] data = new int[N];
            long sum = 0;

            for (int i = 0; i < N; i++) {
                data[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 0; i < N - 1; i++) {
                for (int j = i + 1; j < N; j++) {
                    sum += gcd(data[i], data[j]);
                }
            }
            sb.append(sum).append('\n');
        }
        System.out.println(sb.toString().trim());
    }

    public static int gcd(int a, int b){
        if(a > b){
            int tmp = b;
            b = a;
            a = tmp;
        }

        while (a % b != 0){
            int tmp = a % b;
            a = b;
            b = tmp;
        }

        return b;
    }
}