import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;
    private static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        List<int[]> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(b < a){
                list.add(new int[]{a, b});
            }
        }



        long res = M;
        list.sort((o1, o2) -> o2[0] - o1[0]);


        int start = list.get(0)[0];
        int dest = list.get(0)[1];

        for (int i = 1; i < list.size(); i++) {
            int now = list.get(i)[0];
            int will = list.get(i)[1];

            if(now >= dest)
                dest = Math.min(dest, will);
            else{
                res += (2L * (start - dest));
                start = now;
                dest = will;
            }
        }

        res += (2L * (start - dest));

        System.out.println(res);
    }
}