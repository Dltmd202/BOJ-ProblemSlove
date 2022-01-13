import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static int T;
    private static StringBuilder sb = new StringBuilder();
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int[] current;
    private static int[] goal;
    private static int[] dx = {1, 2, 2, 1, -1, -2, -2, -1};
    private static int[] dy = {-2, -1, 1, 2, 2, 1, -1, -2};


    public static void main(String[] args) throws IOException {
        sb = new StringBuilder();
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int[] current = new int[2];
        int[] goal = new int[2];

        for(int tc = 0; tc < T; tc ++){
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            current[0] = Integer.parseInt(st.nextToken());
            current[1] = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            goal[0] = Integer.parseInt(st.nextToken());
            goal[1] = Integer.parseInt(st.nextToken());

            Queue<int[]> q = new LinkedList<>();
            q.offer(new int[]{current[0], current[1], 0});
            boolean[][] visited = new boolean[N][N];

            while(!q.isEmpty()){
                int[] now = q.poll();
                if(now[0] == goal[0] && now[1] == goal[1]){
                    sb.append(now[2]).append("\n");
                    break;
                }
                for(int i = 0; i < 8; i ++){
                    int ny = now[0] + dy[i];
                    int nx = now[1] + dx[i];

                    if(0 <= ny && ny < N && 0 <= nx && nx < N){
                        if(!visited[ny][nx]){
                            visited[ny][nx] = true;
                            q.offer(new int[]{ny, nx, now[2] + 1});
                        }
                    }
                }
            }
        }

        System.out.println(sb.toString());
    }
}
