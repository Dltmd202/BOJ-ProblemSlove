import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] map = new int[n + 1][m + 1];
        Rotator[] rotators = new Rotator[k];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            rotators[i] = new Rotator(r, c, s);

        }

        System.out.println(backTracking(map, new boolean[k], rotators, k));
    }

    public static int backTracking(int[][] map, boolean[] visited, Rotator[] rotators, int cnt){
        if(cnt == 0){
            int res = Integer.MAX_VALUE;
            for (int i = 1; i < map.length; i++) {
                int sum = 0;
                for (int j = 1; j < map[0].length; j++) {
                    sum += map[i][j];
                }
                res = Math.min(res, sum);
            }
            return res;
        }

        int tmp = Integer.MAX_VALUE;
        for (int i = 0; i < rotators.length; i++) {
            if(!visited[i]){
                visited[i] = true;
                rotate(map, rotators[i]);
                tmp = Math.min(tmp, backTracking(map, visited, rotators, cnt - 1));
                visited[i] = false;
                rotateReverse(map, rotators[i]);
            }
        }
        return tmp;
    }

    public static void rotate(int[][] map, Rotator rotator){
        int r = rotator.r;
        int c = rotator.c;
        int s = rotator.s;
        for (int i = 1; i <= s; i++) {
            int tmp = map[r - i][c - i];
            for (int j = r - i; j < r + i; j++) {
                map[j][c - i] = map[j + 1][c - i];
            }
            for (int j = c - i; j < c + i; j++) {
                map[r + i][j] = map[r + i][j + 1];
            }
            for (int j = r + i; j > r - i; j--) {
                map[j][c + i] = map[j - 1][c + i];
            }
            for (int j = c + i; j > c - i; j--) {
                map[r - i][j] = map[r - i][j - 1];
            }
            map[r - i][c - i + 1] = tmp;
        }
    }

    public static void rotateReverse(int[][] map, Rotator rotator){
        int r = rotator.r;
        int c = rotator.c;
        int s = rotator.s;
        for (int i = 1; i <= s; i++) {
            int tmp = map[r - i][c - i];
            for (int j = c - i; j < c + i; j++) {
                map[r - i][j] = map[r - i][j + 1];
            }
            for (int j = r - i; j < r + i; j++) {
                map[j][c + i] = map[j + 1][c + i];
            }
            for (int j = c + i; j > c - i; j--) {
                map[r + i][j] = map[r + i][j - 1];
            }
            for (int j = r + i; j > r - i; j--) {
                map[j][c - i] = map[j - 1][c - i];
            }
            map[r - i + 1][c - i] = tmp;
        }
    }


    static class Rotator{
        int r;
        int c;
        int s;

        public Rotator(int r, int c, int s) {
            this.r = r;
            this.c = c;
            this.s = s;
        }
    }
}
