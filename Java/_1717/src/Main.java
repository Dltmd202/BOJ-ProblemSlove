import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int find(int[] parents, int x){
        if(parents[x] != x)
            parents[x] = find(parents, parents[x]);
        return parents[x];
    }

    public static void union(int[] parents, int a, int b){
        int A = find(parents, a);
        int B = find(parents, b);

        if(A > B)
            parents[A] = B;
        else
            parents[B] = A;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] parents = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int order = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(order == 0)
                union(parents, a, b);
            else if(order == 1){
                int A = find(parents, a);
                int B = find(parents, b);

                sb.append(A == B ? "YES": "NO").append("\n");
            }
        }

        System.out.println(sb.toString().trim());

    }
}
