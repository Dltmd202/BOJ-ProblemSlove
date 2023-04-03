import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int T;
    private static int[] dx = {0, 0, 1, -1};
    private static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        T = Integer.parseInt(br.readLine());


        while (T-->0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int W = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());

            char[][] map = new char[H][];

            for (int i = 0; i < H; i++) {
                map[i] = br.readLine().toCharArray();
            }

            int res = search(W, H, map);
            sb.append(res != -1 ? res: "IMPOSSIBLE").append("\n");

        }
        System.out.println(sb.toString().trim());
    }

    public static int search(int W, int H, char[][] map){
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[H][W];
        int fireCnt = 0;
        int manCnt = 0;
        int[] start = null;

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if(map[i][j] == '*') {
                    q.offer(new int[]{i, j});
                    fireCnt++;
                }
                else if(map[i][j] == '@') {
                    start = new int[]{i, j, 0};
                    visited[i][j] = true;
                    map[i][j] = '.';
                    manCnt++;
                }
            }
        }


        q.offer(start);

//        System.out.println();
//        System.out.println("Initial State");
//        for (int i = 0; i < H; i++) {
//            System.out.println(Arrays.toString(map[i]));
//        }
//
//        System.out.println("fireCnt = " + fireCnt);
//        System.out.println("manCnt = " + manCnt);
//        for (int[] ints : q) {
//            System.out.println(Arrays.toString(ints));
//        }
//        System.out.println();


        while (!q.isEmpty()){
            int newFireCnt = 0;
            int newManCnt = 0;

            for (int i = 0; i < fireCnt; i++) {
                int[] fire = q.poll();

                for (int j = 0; j < 4; j++) {
                    int ny = fire[0] + dy[j];
                    int nx = fire[1] + dx[j];

                    if(!isInBuilding(H, W, ny, nx)) continue;

                    if(map[ny][nx] == '.'){
                        q.offer(new int[]{ny, nx});
                        map[ny][nx] = '*';
                        newFireCnt++;
                    }
                }
            }


            for (int i = 0; i < manCnt; i++) {
                int[] man = q.poll();

                for (int j = 0; j < 4; j++) {
                    int ny = man[0] + dy[j];
                    int nx = man[1] + dx[j];

                    if(!isInBuilding(H, W, ny, nx)){
                        return man[2] + 1;
                    }

                    if(map[ny][nx] == '.' && !visited[ny][nx]){
                        q.offer(new int[]{ny, nx, man[2] + 1});
                        visited[ny][nx] = true;
                        newManCnt++;
                    }
                }
            }
            fireCnt = newFireCnt;
            manCnt = newManCnt;

//            System.out.println();
//
//            for (int i = 0; i < H; i++) {
//                System.out.println(Arrays.toString(map[i]));
//            }
//
//            System.out.println("fireCnt = " + fireCnt);
//            System.out.println("manCnt = " + manCnt);
//            for (int[] ints : q) {
//                System.out.println(Arrays.toString(ints));
//            }

        }

        return -1;
    }

    public static boolean isInBuilding(int H, int W, int y, int x){
        if(0 > x || x >= W || 0 > y || y >= H) return false;
        return true;
    }


}