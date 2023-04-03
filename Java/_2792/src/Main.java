import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int M;
    private static int[] jw;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        jw = new int[M];

        int min = 1;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < M; i++) {
            jw[i] = Integer.parseInt(br.readLine());
            max = Math.max(max, jw[i]);
        }

        int res = max;
        while (min <= max){
            int mid = min + (max - min) / 2;

            if (N >= getSatisfiedKid(mid)){
                res = mid;
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(res);
    }

    public static int getSatisfiedKid(int x){
        int res = 0;

        for (int i = 0; i < M; i++) {
            if(jw[i] % x == 0){
                res += jw[i] / x;
            } else {
                res += jw[i] / x + 1;
            }
        }

        return res;
    }
}