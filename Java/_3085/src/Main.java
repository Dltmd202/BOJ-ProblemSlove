import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] dy = {0, 1, -1, 0, 0};
    static int[] dx = {0, 0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[][] map = new char[N][N];
        int res = 0;

        for (int i = 0; i < N; i++) {
            map[i] = br.readLine().toCharArray();
        }

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                char origin = map[y][x];
                for (int k = 0; k < 5; k++) {
                    int sy = y + dy[k];
                    int sx = x + dx[k];

                    if(0 > sy || sy >= N || 0 > sx || sx >= N) continue;

                    char tmp = map[sy][sx];
                    map[y][x] = map[sy][sx];
                    map[sy][sx] = origin;


                    res = Math.max(res, count(map, y, x));

                    map[y][x] = origin;
                    map[sy][sx] = tmp;
                }
            }
        }

        System.out.println(res);
    }

    static int count(char[][] map, int y, int x){
        int ver = 0, hol = 0;
        int verMax = 0, holMax = 0;
        for (int i = 0; i < map.length; i++) {
            if(map[y][i] == map[y][x]) hol++;
            else hol = 0;
            if(map[i][x] == map[y][x]) ver++;
            else ver = 0;
            verMax = Math.max(verMax, ver);
            holMax = Math.max(holMax, hol);
        }
        return Math.max(verMax, holMax);
    }
}