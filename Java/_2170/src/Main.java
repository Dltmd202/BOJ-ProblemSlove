import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static long[][] lines;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        lines = new long[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long x = Long.parseLong(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            lines[i][0] = x;
            lines[i][1] = y;
        }

        Arrays.sort(lines, new Comparator<long[]>() {
            @Override
            public int compare(long[] o1, long[] o2) {
                if(o1[0] == o2[0]) return (int) (o1[1] - o2[1]);
                else return (int) (o1[0] - o2[0]);
            }
        });

        long min = lines[0][0];
        long max = lines[0][1];
        long len = max - min;

        for (int i = 1; i < N ; i++) {
            if(min <= lines[i][0] && lines[i][1] <= max) continue;
            else if(lines[i][0] < max){
                len += lines[i][1] - max;
            } else {
                len += lines[i][1] - lines[i][0];
            }
            min = lines[i][0];
            max = lines[i][1];
        }

        System.out.println(len);

    }
}