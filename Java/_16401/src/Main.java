import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 하 https://www.acmicpc.net/problem/2792
 * 중 https://www.acmicpc.net/problem/1477
 * 상 https://www.acmicpc.net/problem/1114
 *
 */
public class Main {

    private static int M;
    private static int N;
    private static int[] snacks;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        snacks = new int[N];

        int min = 1;
        int max = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            snacks[i] = Integer.parseInt(st.nextToken());
            max = Math.max(max, snacks[i]);
        }

        int res = 0;
        while (min <= max) {
            int mid = min + (max - min) / 2;
//            System.out.println(min + " " + mid + " " + max);
//            System.out.println(isPossibleToProvide(mid));

            if(isPossibleToProvide(mid)){
                min = mid + 1;
                res = mid;
            } else {
                max = mid - 1;
            }
        }
        System.out.println(res);
    }

    public static boolean isPossibleToProvide(int x){
        int cnt = 0;
        for (int snack : snacks) {
            cnt += (snack / x);
        }

        return M <= cnt;
    }
}