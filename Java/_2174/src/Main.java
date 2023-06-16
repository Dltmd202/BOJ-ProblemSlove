import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int M;
    private static Map<String, Integer> directionMapper = new HashMap<>();
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    private static int A;
    private static int B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        directionMapper = new HashMap<>();

        directionMapper.put("S", 0);
        directionMapper.put("E", 1);
        directionMapper.put("N", 2);
        directionMapper.put("W", 3);


        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        int[][] board = new int[B + 1][A + 1];

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        Robot[] robots = new Robot[N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            robots[i] = new Robot();
            robots[i].x = Integer.parseInt(st.nextToken());
            robots[i].y = Integer.parseInt(st.nextToken());
            robots[i].dir = directionMapper.get(st.nextToken());
            board[robots[i].y][robots[i].x] = i;
        }

        String answer = "OK";
        boolean res = false;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            String cmd = st.nextToken();
            int times = Integer.parseInt(st.nextToken());

            for (int j = 0; j < times; j++) {
                if(cmd.equals("F")){
                    int ny = robots[id].y + dy[robots[id].dir];
                    int nx = robots[id].x + dx[robots[id].dir];

                    if(1 <= ny && ny <= B && 1 <= nx && nx <= A){

                        if(board[ny][nx] != 0){
                            answer = String.format("Robot %d crashes into robot %d", id, board[ny][nx]);
                            res = true;
                            break;
                        }

                        board[robots[id].y][robots[id].x] = 0;
                        robots[id].y = ny;
                        robots[id].x = nx;
                        board[ny][nx] = id;
                    } else {
                        answer = String.format("Robot %d crashes into the wall", id);
                        res = true;
                        break;
                    }
                }else{
                    robots[id].turn(cmd);
                }
            }


            if(res) break;
        }

        System.out.println(answer.trim());
    }

    static class Robot{
        int y;
        int x;
        int dir;

        void turn(String cmd){
            if(cmd.equals("R")){
                dir = (dir - 1 + 4) % 4;
            } else
                dir = (dir + 1) % 4;
        }
    }
}
