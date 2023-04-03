import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;
    private static int[][] room;
    private static int res;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        room = new int[N][2];

        Queue<int[]> meeting = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] == o2[0]) return o1[1] - o2[1];
                return o1[0] - o2[0];
            }
        });
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            room[i][0] = Integer.parseInt(st.nextToken());
            room[i][1] = Integer.parseInt(st.nextToken());
            meeting.offer(room[i]);
        }

        Queue<int[]> continued = new PriorityQueue<>(((o1, o2) -> o1[1] - o2[1]));

        int max = 0;

        while (!meeting.isEmpty()){
            int[] next = meeting.poll();
            continued.offer(next);

            while (!meeting.isEmpty() && next[0] == meeting.peek()[0]){
                continued.offer(meeting.poll());
            }

            while (!continued.isEmpty() && continued.peek()[1] <= next[0]){
                continued.poll();
            }

            max = Math.max(max, continued.size());
        }

        System.out.println(max);

    }
}