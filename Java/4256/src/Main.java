import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static int T;
    private static List<int[]> answer;
    private static int[] postOrder;
    private static int[] inOrder;
    private static int[] preOrder;
    private static int[] pre2InIndex;
    private static int[] inOrderIndex;
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        answer = new ArrayList<>();
        T = Integer.parseInt(st.nextToken());
        for(int tc = 0; tc < T; tc ++){
            N = Integer.parseInt(br.readLine());
            inOrderIndex = new int[N + 2];

            inOrder = new int[N];
            preOrder = new int[N];
            postOrder = new int[N];
            pre2InIndex = new int[N];

            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < N; i ++) {
                preOrder[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < N; i ++){
                inOrder[i] = Integer.parseInt(st.nextToken());
                inOrderIndex[inOrder[i]] = i;
            }
            for(int i = 0; i < N; i ++){
                pre2InIndex[i] = inOrderIndex[preOrder[i]];
            }
            makeMap(0, N - 1, 0, N - 1, 0);
            answer.add(postOrder);
        }

        for(int[] ans: answer){
            for(int a: ans){
                System.out.print(a + " ");
            }
            System.out.println();
        }
    }
    private static void makeMap(int pl, int pr, int il, int ir, int stepBack){
        if(pl >= 0 && il >= 0 && pl <= pr && il <= ir && pr < N && ir < N) {
            postOrder[ir - stepBack] = preOrder[pl];
            int lcnt = pre2InIndex[pl] - il;
            makeMap(pl + 1, pl + lcnt, il, il + lcnt - 1, stepBack);
            makeMap(pl + lcnt + 1, pr,pre2InIndex[pl] + 1, ir, stepBack + 1);
        }

    }

}
