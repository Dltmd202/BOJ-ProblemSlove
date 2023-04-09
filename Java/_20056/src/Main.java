import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int N;
    public static List<FireBall> list;
    public static Queue<FireBall>[][] map;

    public static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    public static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        list = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int m = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            list.add(new FireBall(r, c, m, d, s));
        }

        map = new Queue[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = new LinkedList<>();

            }
        }

        while (K-- > 0) {
            move();
            combineAndDivide();
        }

        int answer = 0;
        for (FireBall f : list) {
            answer += f.m;
        }
        System.out.print(answer);
    }

    public static void move() {
        for (FireBall f : list) {
            f.r = (N + f.r + dr[f.d] * (f.s % N)) % N;
            f.c = (N + f.c + dc[f.d] * (f.s % N)) % N;

            map[f.r][f.c].add(f);
        }
    }

    public static void combineAndDivide() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j].size() >= 2) {
                    int m_sum = 0, s_sum = 0;
                    int cnt_sum = map[i][j].size();
                    boolean odd = true, even = true;

                    while (!map[i][j].isEmpty()) {
                        FireBall f = map[i][j].poll();
                        m_sum += f.m;
                        s_sum += f.s;

                        if (f.d % 2 == 0) {
                            odd = false;
                        } else {
                            even = false;
                        }
                        list.remove(f);
                    }

                    int nm = m_sum / 5;

                    if (nm == 0)
                        continue;

                    int ns = s_sum / cnt_sum;

                    if (odd | even) {
                        for (int k = 0; k < 8; k += 2) {
                            list.add(new FireBall(i, j, nm, k, ns));
                        }
                    } else {
                        for (int k = 1; k < 8; k += 2) {
                            list.add(new FireBall(i, j, nm, k, ns));
                        }
                    }
                } else {
                    map[i][j].clear();
                }
            }
        }
    }

    public static class FireBall {
        int r, c, m, d, s;

        public FireBall(int r, int c, int m, int d, int s) {
            this.r = r;
            this.c = c;
            this.m = m;
            this.d = d;
            this.s = s;
        }
    }

}
