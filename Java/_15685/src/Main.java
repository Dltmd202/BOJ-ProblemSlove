import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        boolean[][] visited = new boolean[101][101];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            int gen = Integer.parseInt(st.nextToken());

            List<Integer> curves = new ArrayList<>();
            curves.add(dir);

            for (int j = 1; j <= gen; j++) {
                int curvsiz = curves.size();
                for (int k = curvsiz - 1; k >= 0; k--) {
                    curves.add(getNextDirection(curves.get(k)));
                }
            }

            int ny = y;
            int nx = x;
            visited[ny][nx] = true;

            for (Integer ndir : curves) {
                nx = nx + dx[ndir];
                ny = ny + dy[ndir];

                if(0 <= nx && nx <= 100 && 0 <= ny && ny <= 100)
                    visited[ny][nx] = true;
            }
        }

        int res = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (visited[i][j] && visited[i][j + 1] && visited[i + 1][j] && visited[i + 1][j + 1]) {
                    res++;
                }
            }
        }

        System.out.println(res);
    }

    static int getNextDirection(int cur){
        return (cur + 1) % 4;
    }
}