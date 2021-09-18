import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long n = Long.parseLong(st.nextToken());
        long m = Long.parseLong(st.nextToken());

        long count5 = powerCount(n, 5L) - powerCount(m, 5L) - powerCount(n - m, 5L);
        long count2 = powerCount(n, 2L) - powerCount(m, 2L) - powerCount(n - m, 2L);
        System.out.println(Math.min(count2, count5));
    }

    static long powerCount(long num, long m){
        long count = 0L;
        long ret = m;
        while (num >= ret) {
            count += (num / ret);
            ret *= m;
        }
        return count;
    }
}
