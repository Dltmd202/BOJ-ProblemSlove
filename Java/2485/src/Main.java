import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[] cordinate;
    private static int[] interval;
    private static int intervalGcd = 0;
    private static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        cordinate = new int[N];
        interval = new int[N - 1];

        for(int i = 0; i < N; i ++){
            st = new StringTokenizer(br.readLine());
            cordinate[i] = Integer.parseInt(st.nextToken());
            if(i > 0){
                interval[i - 1] = cordinate[i] - cordinate[i - 1];
            }
        }
        intervalGcd = gcd(interval[0], interval[1]);

        for(int i = 2; i < N - 1; i ++){
            intervalGcd = gcd(intervalGcd, interval[i]);
        }

        for(int i = 0; i < N - 1; i ++){
            answer += (interval[i] / intervalGcd - 1);
        }

        System.out.println(answer);
    }

    private static int gcd(int p, int q){
        if(q == 0) return p;
        return gcd(q, p % q);
    }
}
