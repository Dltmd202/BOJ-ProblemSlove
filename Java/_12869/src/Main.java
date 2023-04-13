import java.io.*;
import java.util.*;
public class Main {
    public static int[][] attack = {
            {9, 3, 1},
            {9, 1, 3},
            {3, 9, 1},
            {3, 1, 9},
            {1, 9, 3},
            {1, 3, 9}
    };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] scv = new int[3];
        int[][][] dp = new int[61][61][61];

        for (int i = 0; i < 61; i++) {
            for (int j = 0; j < 61; j++) {
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);
            }
        }



        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            scv[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(scv);
        int buf = scv[0];
        scv[0] = scv[2];
        scv[2] = buf;

        System.out.println(dfs(dp, scv, 0));
    }

    public static int dfs(int[][][] dp, int[] scv, int cnt){
        boolean res = false;
        for (int i = 0; i < scv.length; i++) {
            if(scv[i] != 0){
                res = true;
                break;
            }
        }

        if(!res) return cnt;

        Arrays.sort(scv);
        int buf = scv[0];
        scv[0] = scv[2];
        scv[2] = buf;

        if(dp[scv[0]][scv[1]][scv[2]] != Integer.MAX_VALUE)
            return dp[scv[0]][scv[1]][scv[2]];

        int tmp = Integer.MAX_VALUE;
        for (int i = 0; i < 6; i++) {
            int[] next = new int[3];
            next[0] = Math.max(scv[0] - attack[i][0], 0);
            next[1] = Math.max(scv[1] - attack[i][1], 0);
            next[2] = Math.max(scv[2] - attack[i][2], 0);

            tmp = Math.min(tmp, dfs(dp, next, cnt + 1));
        }

        dp[scv[0]][scv[1]][scv[2]] = tmp;
        return tmp;
    }


}
