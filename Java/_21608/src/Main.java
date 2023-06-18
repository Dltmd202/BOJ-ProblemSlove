import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[] dy = {1, -1, 0, 0};
    static int[] dx = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] map  = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(map[i], -1);
        }

        List<Integer>[] graph = new List[N * N + 2];

        for (int k = 0; k < N * N; k++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int target = Integer.parseInt(st.nextToken());
            List<Integer> members = new ArrayList<>();
            while (st.hasMoreTokens()){
                members.add(Integer.parseInt(st.nextToken()));
            }
            graph[target] = members;

            int[][] prefers = new int[N][N];
            int[][] blanks = new int[N][N];

            for (int i = 0; i < N; i++) {
                Arrays.fill(prefers[i], -1);
                Arrays.fill(blanks[i], -1);
            }

            int maxPrefer = 0;
            int minPrefer = Integer.MAX_VALUE;
            int maxBlank = 0;
            int minBlank = Integer.MAX_VALUE;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    int prefer = 0;
                    int blank = 0;
                    if(map[i][j] != -1) continue;
                    for (int l = 0; l < 4; l++) {
                        int ny = i + dy[l];
                        int nx = j + dx[l];

                        if(0 > ny || ny >= N || 0 > nx || nx >= N) continue;
                        if(map[ny][nx] == -1) blank++;
                        for(int pref : members){
                            if(map[ny][nx] == pref) {
                                prefer++;
                                break;
                            }
                        }
                    }

                    prefers[i][j] = prefer;
                    blanks[i][j] = blank;

                    maxPrefer = Math.max(maxPrefer, prefer);
                    minPrefer = Math.min(minPrefer, prefer);

                    maxBlank = Math.max(maxBlank, blank);
                    minBlank = Math.min(minBlank, blank);
                }
            }

            if(maxPrefer > 0){
                boolean res = false;
                int blankCheck = Integer.MIN_VALUE;
                int y = 0;
                int x = 0;
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if(prefers[i][j] == maxPrefer) {
                            if(blanks[i][j] > blankCheck){
                                blankCheck = blanks[i][j];
                                y = i;
                                x = j;
                            }
                        }
                    }
                }

                map[y][x] = target;

            } else {
                boolean res = false;

                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if(blanks[i][j] == maxBlank){
                            map[i][j] = target;
                            res = true;
                            break;
                        }
                    }
                    if(res) break;
                }
            }

        }


        int score = 0;



        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int target = map[i][j];

                int prefer = 0;
                for (int k = 0; k < 4; k++) {
                    int ny = i + dy[k];
                    int nx = j + dx[k];

                    if(0 > ny || ny >= N || 0 > nx || nx >= N) continue;
                    for(int pref : graph[target]){
                        if(map[ny][nx] == pref) {
                            prefer++;
                            break;
                        }
                    }
                }
                if(prefer > 0){
                    score += Math.pow(10, prefer - 1);
                }
            }
        }

        System.out.println(score);
    }
}