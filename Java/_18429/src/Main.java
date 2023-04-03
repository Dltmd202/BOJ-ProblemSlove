import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int K;
    static int[] kits;
    static int answer;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        kits = new int[N];
        visited = new boolean[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            kits[i] = Integer.parseInt(st.nextToken());
        }

        search(new ArrayList<>(), 500);

        System.out.println(answer);
    }

    public static void search(List<Integer> set, int weight){
        if(set.size() == N){
            answer++;
        }

        for (int i = 0; i < N; i++) {
            if(weight - K + kits[i] < 500) continue;
            if(visited[i]) continue;

            set.add(i);
            visited[i] = true;
            search(set, weight - K + kits[i]);
            set.remove(set.size() - 1);
            visited[i] = false;
        }
    }
}