import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int[] durability = new int[N * 2];
        boolean[] isRobot = new boolean[N * 2];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 2 * N; i++) {
            durability[i] = Integer.parseInt(st.nextToken());
        }

        int turn = 0;
        List<Integer> robots = new ArrayList<>();
        List<Integer> tmp;

        while (true){
            turn++;

            int entrance = getEntrance(N, turn);
            int exit = getExit(N, turn);

            int curRobotCnt = robots.size();
            tmp = new ArrayList<>();
            for (int i = 0; i < curRobotCnt; i++) {
                int current = robots.get(i);
                if(current == exit){
                    isRobot[current] = false;
                } else {
                    tmp.add(current);
                }
            }
            robots = tmp;


            curRobotCnt = robots.size();
            tmp = new ArrayList<>();
            for (int i = 0; i < curRobotCnt; i++) {
                int current = robots.get(i);
                int next = getNextBelt(N, current);

                if(next == exit && durability[next] > 0) {
                    isRobot[current] = false;
                    durability[next]--;
                } else {
                    if(!isRobot[next] && durability[next] > 0){
                        isRobot[current] = false;
                        isRobot[next] = true;
                        durability[next]--;

                        tmp.add(next);
                    } else{
                        tmp.add(current);
                    }

                }
            }
            robots = tmp;

            if(durability[entrance] > 0){
                isRobot[entrance] = true;
                durability[entrance]--;
                robots.add(entrance);
            }

            if(hasFinished(K, durability))
                break;

        }

        System.out.println(turn);
    }

    public static int getEntrance(int N, int turn){
        return ((-turn % (N * 2)) + 2 * N) % (N * 2);
    }

    public static int getExit(int N, int turn){
        return (((-turn - N - 1) % (N * 2)) + 2 * N) % (N * 2);
    }

    public static int getNextBelt(int N, int cur){
        return (cur + 1) % (2 * N);
    }

    public static boolean hasFinished(int K, int[] dub){
        return Arrays.stream(dub).filter(a -> a <= 0).count() >= K;
    }



}
