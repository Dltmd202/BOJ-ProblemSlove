import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int M = (int) Math.log10(N) + 1;

        boolean[][] visited = new boolean[1000001][K + 1];

        Queue<Node> q = new ArrayDeque<>();

        q.add(new Node(N, 0));
        visited[N][0] = true;

        int res = -1;

        while (!q.isEmpty()) {
            Node cur = q.poll();

            if(cur.depth == K){
                res = Math.max(res, cur.number);
                continue;
            }

            for (int i = 0; i < M - 1; i++) {
                for (int j = i + 1; j < M; j++) {
                    int switchedNumber = getSwitchedNumber(cur.number, i, j);

                    if (switchedNumber != -1 && !visited[switchedNumber][cur.depth + 1]) {
                        visited[switchedNumber][cur.depth + 1] = true;
                        q.add(new Node(switchedNumber, cur.depth + 1));
                    }
                }
            }
        }

        System.out.println(res);
    }

    static class Node{
        int number;
        int depth;

        public Node(int number, int depth) {
            this.number = number;
            this.depth = depth;
        }
    }

    private static int getSwitchedNumber(int number, int i, int j) {
        char[] charNumber = String.valueOf(number).toCharArray();

        if (i == 0 && charNumber[j] == '0')
            return -1;

        char tmp = charNumber[i];
        charNumber[i] = charNumber[j];
        charNumber[j] = tmp;

        return Integer.parseInt(new String(charNumber));
    }
}