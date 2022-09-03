import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        System.out.println(solution(n));
    }

    private static long solution(int n) {
        Queue<Long> q = new LinkedList<>();
        q.offer(0L);

        for (long i = 0; i <= 9; i++) {
            q.offer(i);
        }

        int cnt = 0;
        while (!q.isEmpty()){
            long now = q.poll();
            if(now > 9876543210L){
                return -1;
            }
            if(cnt++ == n){
                return now;
            }

            for (int i = 0; i < now % 10; i++) {
                q.offer(now * 10 + i);
            }
        }
        return -1;
    }
}