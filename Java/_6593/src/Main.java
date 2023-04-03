import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static int[] dy = {1, -1, 0, 0, 0, 0};
    private static int[] dx = {0, 0, 1, -1, 0, 0};
    private static int[] dz = {0, 0, 0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();


        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int L = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            if(L == 0 && R == 0 && C == 0) break;


            char[][][] map = new char[L][R][];
            boolean[][][] visited = new boolean[L][R][C];
            Queue<int[]> q = new ArrayDeque<>();
            int[] e = new int[3];

            for (int i = 0; i < L; i++) {
                for (int j = 0; j < R; j++) {
                    map[i][j] = br.readLine().toCharArray();

                    for (int k = 0; k < C; k++) {
                        if(map[i][j][k] == '#' || map[i][j][k] == '.') continue;
                        if(map[i][j][k] == 'S'){
                            q.offer(new int[] {i, j, k, 0});

                            map[i][j][k] = '.';
                            visited[i][j][k] = true;
                        }
                        else if(map[i][j][k] == 'E'){
                            e = new int[] {i, j, k};
                        }
                    }
                }
                br.readLine();
            }

            int res = -1;
            app:while (!q.isEmpty()){
                int[] cur = q.poll();

                for (int i = 0; i < 6; i++) {
                    int nz = cur[0] + dz[i];
                    int ny = cur[1] + dy[i];
                    int nx = cur[2] + dx[i];

                    if(!isValidArea(L, R, C, nz, ny, nx)) continue;

                    if(isEscape(e, nz, ny, nx)) {
                        res = cur[3] + 1;
                        break app;
                    }

                    if(!visited[nz][ny][nx] && map[nz][ny][nx] == '.'){
                        visited[nz][ny][nx] = true;
                        q.offer(new int[]{nz, ny, nx, cur[3] + 1});
                    }

                }
            }

            sb.append(res == -1 ? "Trapped!" : String.format("Escaped in %d minute(s).", res))
                    .append("\n");
        }

        System.out.println(sb.toString().trim());
    }

    public static boolean isValidArea(int L, int R, int C, int z, int y, int x){
        return 0 <= z && z < L && 0 <= y && y < R && 0 <= x && x < C;
    }

    public static boolean isEscape(int[] e, int z, int y, int x){
        return Arrays.equals(e, new int[]{z, y, x});
    }
}