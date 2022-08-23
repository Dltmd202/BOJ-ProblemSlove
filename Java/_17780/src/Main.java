import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] dy = new int[]{0, 0, 0, -1, 1};
    static int[] dx = new int[]{0, 1, -1, 0, 0};
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException{
        System.out.println(solution());
    }

    private static int solution() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Piece>[][] cur = new Queue[n + 1][n + 1];
        int[][] map = new int[n + 1][n + 1];
        List<Piece> pieces = new ArrayList<>();
        Stack<Piece> buffer = new Stack<>();
        pieces.add(new Piece());

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                cur[i][j] = new LinkedList<>();
            }
        }

        for (int i = 1; i <= k; i++) {
            st = new StringTokenizer(br.readLine());
            Piece newPiece = new Piece(
                    i,
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    DirectionUtil.findDirection(Integer.parseInt(st.nextToken()))
            );
            cur[newPiece.y][newPiece.x].add(newPiece);
            pieces.add(newPiece);
        }
        
        int turn = 0;
        while (true){
            boolean res = false;
            turn++;
            if(turn >= 1000) break;
            for (int i = 1; i <= k; i++) {
                Piece curPiece = pieces.get(i);
                int curY = curPiece.y;
                int curX = curPiece.x;
                Direction curDirection = curPiece.dir;

                if(cur[curY][curX].peek() != curPiece) continue;
                
                int ny = curY + dy[curDirection.id];
                int nx = curX + dx[curDirection.id];
                if(ny < 1 || n < ny || nx < 1 || n < nx || map[ny][nx] == 2){
                    curPiece.dir = DirectionUtil.reverseDirection(curDirection);
                    ny = curY + dy[curPiece.dir.id];
                    nx = curPiece.x + dx[curPiece.dir.id];
                    
                }
                
                if(ny < 1 || n < ny || nx < 1 || n < nx || map[ny][nx] == 2){
                    continue;
                }
                else if(map[ny][nx] == 0){
                    while(!cur[curY][curX].isEmpty()){
                        Piece poll = cur[curY][curX].poll();
                        poll.y = ny;
                        poll.x = nx;
                        cur[ny][nx].offer(poll);
                    }
                } else if(map[ny][nx] == 1){
                    while (!cur[curY][curX].isEmpty()){
                        Piece poll = cur[curY][curX].poll();
                        poll.y = ny;
                        poll.x = nx;
                        buffer.push(poll);
                    }
                    while (!buffer.isEmpty()){
                        Piece poll = buffer.pop();
                        cur[ny][nx].offer(poll);
                    }
                }

                if(cur[curPiece.y][curPiece.x].size() >= 4){
                    return turn;
                }
                
            }
        }
        return -1;
    }

    static class DirectionUtil{
        public static Direction reverseDirection(Direction dir){
            if(dir == Direction.RIGHT){
                return Direction.LEFT;
            } else if(dir == Direction.LEFT){
                return Direction.RIGHT;
            } else if(dir == Direction.UP){
                return Direction.DOWN;
            } else if(dir == Direction.DOWN){
                return Direction.UP;
            }
            return null;
        }
        
        public static Direction findDirection(int id){
            if(id == 1) return Direction.RIGHT;
            else if(id == 2) return Direction.LEFT;
            else if(id == 3) return Direction.UP;
            else if(id == 4) return Direction.DOWN;
            return null;
        }
        
    }
    
    static class Piece{
        public int id;
        public int y;
        
        public int x;
        public Direction dir;

        @Override
        public String toString() {
            return "{" +
                    "id=" + id +
                    ", y=" + y +
                    ", x=" + x +
                    ", dir=" + dir +
                    '}';
        }

        public Piece(){}

        public Piece(int id, int y, int x, Direction dir) {
            this.id = id;
            this.y = y;
            this.x = x;
            this.dir = dir;
        }
        
    } 
    enum Direction{
        RIGHT(1),
        LEFT(2),
        UP(3),
        DOWN(4);

        public int id;

        Direction(int id) {
            this.id = id;
        }
    }
}