import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int M;
    private static int[][] map;
    private static int res = 0;


    private static int[][][] frame = new int[][][]{
            {{0, 0, 1}, {-1, 0, 0}},
            {{0, 0, -1}, {-1, 0, 0}},
            {{-1, 0, 0}, {0, 0, 1}},
            {{1, 0, 0}, {0, 0, 1}}
    };
    private static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        search(0, 0,0);
        System.out.println(res);
    }

    public static void search(int sy, int sx, int hard){
        int ret = 0;


        for (int y = sy; y < N; y++) {
            for (int x = sx; x < M; x++) {
//                System.out.println(indent + y + " " + x);
                if(visited[y][x]) continue;

                for (int i = 0; i < 4; i++) {
                    boolean suc = true;
                    for (int j = 0; j < 3; j++) {
                        int ny = y + frame[i][0][j];
                        int nx = x + frame[i][1][j];

                        if(0 > ny || ny >= N || 0 > nx || nx >= M || visited[ny][nx])
                            suc = false;
                    }

                    if(!suc) continue;

                    int curHard = map[y][x];
                    for (int j = 0; j < 3; j++) {
                        int ny = y + frame[i][0][j];
                        int nx = x + frame[i][1][j];

                        visited[ny][nx] = true;
                        curHard += map[ny][nx];
                    }

//                    for (int j = 0; j < N; j++) {
//                        System.out.println(indent + Arrays.toString(visited[j]));
//                    }
//                    System.out.println();

                    res = Math.max(res, curHard + hard);
                    search( y, x + 1, curHard + hard);


                    for (int j = 0; j < 3; j++) {
                        int ny = y + frame[i][0][j];
                        int nx = x + frame[i][1][j];

                        visited[ny][nx] = false;
                    }


                }
            }
            sx = 0;
        }
//        System.out.println(indent + "end");

    }
}