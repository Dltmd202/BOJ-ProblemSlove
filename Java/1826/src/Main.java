import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static class GasStation implements Comparable<GasStation> {
        int dist;
        int fuel;
        GasStation next;

        public GasStation(int dist, int fuel) {
            this.dist = dist;
            this.fuel = fuel;
        }

        public GasStation(int dist, int fuel, GasStation next) {
            this.dist = dist;
            this.fuel = fuel;
            this.next = next;
        }

        @Override
        public int compareTo(GasStation o) {
            return this.dist - o.dist;
        }

        @Override
        public String toString() {
            return "GasStation{" +
                    "dist=" + dist +
                    ", fuel=" + fuel +
                    ", next=" + next +
                    '}';
        }
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Queue<GasStation> stations = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            stations.offer(new GasStation(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            ));
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        int l = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        Queue<Integer> fuels = new PriorityQueue<>(Collections.reverseOrder());

        System.out.println(search(stations, l, p, fuels));

    }

    private static int search(Queue<GasStation> stations, int l, int p, Queue<Integer> fuels) {
        int answer = 0;
        while (p < l) {
            System.out.println(stations);
            System.out.println(fuels);
            while (!stations.isEmpty() && stations.peek().dist <= p) {
                fuels.add(stations.poll().fuel);
            }
            if (fuels.isEmpty()) {
                return -1;
            }
            answer++;
            p += fuels.poll();
        }
        return answer;
    }


}