import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;
    private static int M;
    private static int L;
    private static List<Integer> list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        list = new ArrayList<>();
        list.add(0);
        list.add(L);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            list.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(list);

        int left = 1;
        int right = L;

        while (left <= right){
            int mid = (left + right) / 2;

            if(canMake(mid)) left = mid + 1;
            else right = mid - 1;
        }

        System.out.println(left);
    }

    public static boolean canMake(int mid) {
        int count = 0;
        for(int i = 1; i < list.size(); i++) {
            count += (list.get(i) - list.get(i - 1) - 1) / mid;
        }
        if(count > M) return true;
        return false;
    }
}