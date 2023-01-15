import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int K;
    static int[][] map;
    static List<Integer>[][] stacked;
    static Piece[] pieces;
    static int[] dy = {0, 0, 0, -1, 1};
    static int[] dx = {0, 1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        map = new int[N + 1][N + 1];
        pieces = new Piece[K + 1];
        stacked = new ArrayList[N + 1][N + 1];

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                stacked[i][j] = new ArrayList<>();
            }
        }

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i <= K; i++) {
            st = new StringTokenizer(br.readLine());
            pieces[i] = new Piece(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
            stacked[pieces[i].y][pieces[i].x].add(i);
        }

//        for (int j = 1; j <= N; j++) {
//            for (int k = 1; k <= N; k++) {
//                System.out.print(stacked[j][k] + " ");
//            }
//            System.out.println();
//        }
//        System.out.println();


        for (int t = 1; t <= 1000; t++) {
//            System.out.println("@@@@@@@@@  " + t + "  @@@@@@@@");
            for (int i = 1; i <= K; i++) {
                int y = pieces[i].y;
                int x = pieces[i].x;
                int dir = pieces[i].dir;

                int ny = y + dy[dir];
                int nx = x + dx[dir];

//                System.out.println(i);
//                System.out.println(y + " " + x);
//                System.out.println("!!!!");
//                System.out.println(ny + " " + nx);

                if(1 > ny || ny >= (N + 1) || 1 > nx || nx >= (N + 1) || map[ny][nx] == 2){
                    int ndir = reverseDirection(dir);
                    pieces[i].dir = ndir;

                    ny = y + dy[ndir];
                    nx = x + dx[ndir];

//                    System.out.println(ny + " " + nx);

                    if(1 > ny || ny >= (N + 1) || 1 > nx || nx >= (N + 1) || map[ny][nx] == 2) continue;
                    if(map[ny][nx] != 2){
                        i--;
                        continue;
                    }
                } else {
                    int curIndex = stacked[y][x].indexOf(i);
                    int len = stacked[y][x].size() - curIndex;
                    int[] tmp = new int[len];

//                    System.out.println(stacked[y][x]);
                    for (int j = 0; j < len; j++) {
                        tmp[j] = stacked[y][x].remove(stacked[y][x].size() - 1);
                    }

                    if(map[ny][nx] == 0){
                        for (int j = len - 1; j >= 0; j--) {
                            stacked[ny][nx].add(tmp[j]);
                            pieces[tmp[j]].y = ny;
                            pieces[tmp[j]].x = nx;
                        }
                    } else {
                        for (int j = 0; j < len; j++) {
                            stacked[ny][nx].add(tmp[j]);
                            pieces[tmp[j]].y = ny;
                            pieces[tmp[j]].x = nx;
                        }
                    }


                }
                if(stacked[ny][nx].size() >= 4){
                    System.out.println(t);
                    System.exit(0);
                }
            }
        }

        System.out.println(-1);

    }

    static class Piece{
        int y;
        int x;
        int dir;

        public Piece(int y, int x, int dir) {
            this.y = y;
            this.x = x;
            this.dir = dir;
        }

        @Override
        public String toString() {
            return "Piece{" +
                    "y=" + y +
                    ", x=" + x +
                    ", dir=" + dir +
                    '}';
        }
    }

    public static boolean checkFinished(){
        Piece first = pieces[1];

        for (int i = 2; i <= K; i++) {
            if(pieces[i].x != first.x || pieces[i].y != first.y) return false;
        }
        return true;
    }

    public static int reverseDirection(int dir){
        if(dir == 1) return 2;
        else if(dir == 2) return 1;
        else if(dir == 3) return 4;
        else return 3;
    }
}