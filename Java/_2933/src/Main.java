import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] dy = {1, -1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        Queue<Node> q = new LinkedList<>();
        char[][] map = new char[r][c];
        int[][] visited;

        for (int i = 0; i < r; i++) {
            char[] line = br.readLine().toCharArray();
            for (int j = 0; j < c; j++) {
                map[i][j] = line[j];
            }
        }

        int cnt = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int turn = 0; turn < cnt; turn++) {
            visited = new int[r][c];
            int h = getHeight(r, Integer.parseInt(st.nextToken()));
            int x = getX(map,  h, turn);
            int seq = 1;
            if(x == -1) continue;
            map[h][x] = '.';

            // 땅 검색
            for (int i = 0; i < map[0].length; i++) {
                if(map[r - 1][i] == 'x' && visited[r - 1][i] == 0){
                    bfs(map, visited, r - 1, i, seq);
                }
            }
            List<Result> results = new ArrayList<>();

            for (int i = 0; i < map.length - 1; i++) {
                for (int j = 0; j < map[0].length; j++) {
                    if(map[i][j] == 'x' && visited[i][j] == 0) {
                        Result result = bfs(map, visited, i, j, ++seq);
                        results.add(result);
                    }
                }
            }

            for (Result result : results) {
                int ableToDownHeight = getAbleToDownHeight(r, visited, seq, result);
                for (Node node : result.nodes) {
                    map[node.y][node.x] = '.';
                }
                for (Node node : result.nodes) {
                    map[node.y + ableToDownHeight][node.x] = 'x';
                }
            }
        }

        for (char[] chars : map) {
            System.out.println(chars);
        }
    }

    private static int getAbleToDownHeight(int r, int[][] visited, int seq, Result result) {
        int ableToDown = Integer.MAX_VALUE;
        for (int x = result.sx; x <= result.ex; x++) {
            int belowLowest = 0;
            int ableToDownRow = 0;
            for (int y = 0; y < r; y++) {
                if(visited[y][x] == seq)
                    belowLowest = y;
            }

            for (int y = belowLowest + 1; y < r; y++) {

                if(visited[y][x] == 1) break;
                ableToDownRow++;
            }
            ableToDown = Math.min(ableToDown, ableToDownRow);
        }
        return ableToDown;
    }

    static class Node{
        int y;
        int x;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static class Result {
        int sx;
        int ex;
        List<Node> nodes = new ArrayList<>();

        public Result(int x) {
            this.sx = x;
            this.ex = x;
        }
    }


    public static Result bfs(char[][] map, int[][] visited, int y, int x, int grad){
        Queue<Node> q = new LinkedList<>();
        visited[y][x] = grad;
        Node snode = new Node(y, x);
        q.offer(snode);
        Result result = new Result(x);
        result.nodes.add(snode);

        while(!q.isEmpty()){
            Node now = q.poll();
            for (int j = 0; j < 4; j++) {
                int ny = now.y + dy[j];
                int nx = now.x + dx[j];

                if(0 > ny || ny >= map.length || 0 > nx || nx >= map[0].length) continue;

                if(map[ny][nx] == 'x' && visited[ny][nx] == 0){
                    Node nnode = new Node(ny, nx);
                    q.offer(nnode);
                    result.nodes.add(nnode);
                    visited[ny][nx] = grad;
                    result.sx = Math.min(result.sx, nx);
                    result.ex = Math.max(result.ex, nx);
                }
            }
        }
        return result;
    }

    public static int getX(char[][] map, int height, int turn){
        if(turn % 2 == 0) {
            for (int i = 0; i < map[0].length; i++) {
                if(map[height][i] == 'x') return i;
            }
        } else {
            for (int i = map[0].length - 1; i >= 0; i--) {
                if(map[height][i] == 'x') return i;
            }
        }
        return -1;
    }

    public static int getHeight(int r, int x){
        return r - x;
    }
}