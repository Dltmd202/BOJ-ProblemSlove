import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        while (T-->0){
            int N = Integer.parseInt(br.readLine());
            List<int[]> ways = new ArrayList<>();

            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] home = new int[]{
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            };

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                ways.add(
                        new int[]{
                                Integer.parseInt(st.nextToken()),
                                Integer.parseInt(st.nextToken())
                        }
                );
            }
            Integer.MAX_VALUE

            st = new StringTokenizer(br.readLine());
            int[] fes = new int[]{
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            };

            sb.append(
                search(N, home, fes, ways)
            ).append("\n");
        }

        System.out.println(sb.toString().trim());
    }

    private static String search(int N, int[] home, int[] fes, List<int[]> store) {
        Queue<int[]> q = new ArrayDeque<>();
        boolean[] visited = new boolean[N];

        q.add(home);

        while (!q.isEmpty()){
            int[] cur = q.poll();

            if(getDistance(cur, fes) <= 1000) {
                return "happy";
            }

            for (int i = 0; i < N; i++) {
                if(!visited[i]){
                    int[] next = store.get(i);
                    int distance = getDistance(cur, next);

                    if(distance <= 1000){
                        visited[i] = true;
                        q.offer(next);
                    }
                }
            }
        }

        return "sad";
    }

    public static int getDistance(int[] a, int[] b){
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
}