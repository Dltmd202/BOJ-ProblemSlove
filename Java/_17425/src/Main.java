import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        long[] fx = new long[1000001];
        long[] gx = new long[1000001];

        Arrays.fill(fx, 1);
        gx[1] = 1;

        for (int i = 2; i <= 1000000; i++) {
            int j = 1;
            while (i * j <= 1000000){
                fx[i * j] += i;
                j++;
            }
            gx[i] = gx[i - 1] + fx[i];
        }

        int T = Integer.parseInt(br.readLine());

        while (T-->0){
            int N = Integer.parseInt(br.readLine());
            sb.append(gx[N]).append("\n");
        }
        System.out.println(sb.toString());
    }
}