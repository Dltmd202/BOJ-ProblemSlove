import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        System.out.println(solution(new int[]{A, B, C}));
    }

    private static int solution(int[] data) {
        if((data[0] + data[1] + data[2]) % 3 != 0) return 0;

        Arrays.sort(data);
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[1501][1501];
        q.offer(data);

        while (!q.isEmpty()){
            int[] cur = q.poll();

            if(cur[0] == cur[1] && cur[1] == cur[2]) return 1;

            for (int i = 0; i < 2; i++) {
                for (int j = i + 1; j < 3; j++) {
                    int target1 = cur[i];
                    int target2 = cur[j];
                    int left = cur[getLeftIdx(i, j)];

                    if(target2 > target1){
                        int tmp = target2;
                        target2 = target1;
                        target1 = tmp;
                    }

                    target1 -= target2;
                    target2 += target2;

                    int[] res = new int[]{target1, target2, left};
                    Arrays.sort(res);

                    if(!visited[target1][target2]){
                        visited[target1][target2] = true;
                        q.offer(res);
                    }
                }
            }
        }

        return 0;
    }

    private static int getLeftIdx(int i, int j){
        if(i < j){
            int tmp = i;
            i = j;
            j = tmp;
        }

        if(i == 2){
            if(j == 1) return 0;
            if(j == 0) return 1;
        }
        return 2;
    }

}