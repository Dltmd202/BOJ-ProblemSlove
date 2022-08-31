import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static char[][] map;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    
    public static void main(String[] args) throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        map = new char[n + 1][];
        for (int i = n; i >= 1; i--) {
            char[] data = br.readLine().toCharArray();
            map[i] = data;
        }
        
        int actionCount = Integer.parseInt(br.readLine());
        int[] actions = new int[actionCount];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < actionCount; i++) {
            actions[i] = Integer.parseInt(st.nextToken());
        }
        
        int turn = 0;
        for(int action: actions){
            if(turn++ % 2 == 0){
                for (int i = 0; i < m; i++) {
                    if(map[action][i] == 'x'){
                        map[action][i] = '.';
                        break;
                    }
                }
            } else {
                for (int i = m - 1; i >= 0; i--) {
                    if(map[action][i] == 'x'){
                        map[action][i] = '.';
                        break;
                    }
                }
            }

            List<Cluster> clusters = new ArrayList<>();
            int[][] visited = new int[map.length + 1][map[1].length];
            int id = 0;
            for (int i = n; i >= 1; i--) {
                for (int j = 0; j < m; j++) {
                    if(visited[i][j] == 0 && map[i][j] == 'x') {
                        clusters.add(bfs(visited, new Coordinate(i, j), ++id));
                    }
                }
            }
            
            for(Cluster cluster : clusters){
                boolean res = false;
                for (Coordinate coordinate : cluster.coordinates) {
                    if(coordinate.y == 1){
                        res = true;
                        break;
                    }
                }
                if(res) continue;
                
                
                int[] minColHeight = new int[m];
                Arrays.fill(minColHeight, Integer.MAX_VALUE);
                for(Coordinate coordinate : cluster.coordinates){
                    if(minColHeight[coordinate.x] > coordinate.y){
                        minColHeight[coordinate.x] = coordinate.y;
                    }
                }
                
                int elevateHeight = Integer.MAX_VALUE;
                for (Coordinate coordinate : cluster.coordinates) {
                    int tmp = 0;

                    while (true){
                        int ny = coordinate.y - (tmp + 1);
                        if(visited[coordinate.y][coordinate.x] == visited[ny][coordinate.x]) {
                            tmp++;
                            continue;
                        }
                        if(ny < 1) break;
                        if(map[ny][coordinate.x] == 'x') {
                            break;
                        }
                        tmp++;
                    }

                    elevateHeight = Math.min(elevateHeight, tmp);
                    if(elevateHeight == 0) break;
                }
                
                for (Coordinate coordinate : cluster.coordinates) {
                    map[coordinate.y][coordinate.x] = '.';
                }
                for (Coordinate coordinate : cluster.coordinates) {
                    map[coordinate.y - elevateHeight][coordinate.x] = 'x';
                }
            }
        }
        for (int i = map.length - 1; i >= 1 ; i--) {
            System.out.println(map[i]);
        }
    }
    
    public static Cluster bfs(int[][] visited, Coordinate start, int id){
        visited[start.y][start.x] = id;
        Queue<Coordinate> q = new LinkedList<>();
        Set<Coordinate> set = new HashSet<>();
        q.offer(start);
        set.add(start);
        
        while (!q.isEmpty()){
            Coordinate now = q.poll();

            for (int i = 0; i < 4; i++) {
                int ny = now.y + dy[i];
                int nx = now.x + dx[i];
                
                if(1 <= ny && ny <= map.length - 1 && 0 <= nx && nx < map[1].length){
                    if(visited[ny][nx] == 0 && map[ny][nx] == 'x') {
                        visited[ny][nx] = id;
                        Coordinate coordinate = new Coordinate(ny, nx);
                        q.offer(coordinate);
                        set.add(coordinate);
                    }
                }
            }
        }
        
        return new Cluster(set);
    }
    
    static class Cluster{
        Set<Coordinate> coordinates;

        public Cluster(Set<Coordinate> coordinates) {
            this.coordinates = coordinates;
        }
    }
    
    static class Coordinate{
        int y;
        int x;
        
        public Coordinate(int y, int x){
            this.y = y;
            this.x = x;
        }
    }
}