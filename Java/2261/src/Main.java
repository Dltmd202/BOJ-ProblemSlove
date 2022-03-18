import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;

    private static Coordinate[] coordinates;

    public static class Coordinate{
        int x;
        int y;

        public int getDistance(int x, int y){
            return (this.x - x) * (this.x - x) + (this.y - y) * (this.y - y);
        }

        public int getDistance(Coordinate coordinate){
            return this.getDistance(coordinate.x, coordinate.y);
        }

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        coordinates = new Coordinate[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            coordinates[i] = new Coordinate(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(coordinates, new Comparator<Coordinate>() {
            @Override
            public int compare(Coordinate o1, Coordinate o2) {
                return o1.x - o2.x;
            }
        });


        System.out.println(crossPair(0, N - 1));
    }

    public static int getDistance(int start, int end){
        int dist = Integer.MAX_VALUE;

        for (int i = start; i < end; i++) {
            for (int j = i + 1; j <= end; j++) {
                int tmp = coordinates[i].getDistance(coordinates[j]);

                dist = Math.min(dist, tmp);
            }
        }
        return dist;
    }

    public static int crossPair(int start, int end){
        if(end - start <= 2){
            return getDistance(start, end);
        }
        int mid = (start + end) / 2;

        int left = crossPair(start, mid);
        int right = crossPair(mid + 1, end);
        int dist = Math.min(left, right);

        List<Coordinate> list = new ArrayList<>();

        for (int i = start; i <= end; i++) {
            int tmp = coordinates[mid].x - coordinates[i].x;

            if (tmp * tmp < dist){
                list.add(coordinates[i]);
            }
        }

        list.sort(new Comparator<Coordinate>() {
            @Override
            public int compare(Coordinate o1, Coordinate o2) {
                return o1.y - o2.y;
            }
        });

        for (int i = 0; i < list.size() - 1; i++) {
            for (int j = i + 1; j < list.size(); j++) {
                int tmp = list.get(i).y - list.get(j).y;

                if (tmp * tmp < dist){
                    dist = Math.min(dist, list.get(i).getDistance(list.get(j)));
                } else {
                    break;
                }
            }
        }
        return dist;
    }
}
