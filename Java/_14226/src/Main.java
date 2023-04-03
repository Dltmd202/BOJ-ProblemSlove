import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int S = sc.nextInt();
        System.out.println(bfs(S));

    }

    private static int bfs(int S) {
        Queue<Board> q = new ArrayDeque<>();
        q.offer(new Board(1, 0, 0));
        Set<Board> visited = new HashSet<>();

        while (!q.isEmpty()){
            Board cur = q.poll();
            if(cur.emo == S) return cur.time;

            Board[]  boards = new Board[]{
                    new Board(cur.emo, cur.emo, cur.time + 1),
                    new Board(cur.emo + cur.clipboard, cur.clipboard, cur.time + 1),
                    new Board(cur.emo - 1, cur.clipboard, cur.time + 1)
            };

            for (Board board : boards) {
                if(!visited.contains(board)){
                    visited.add(board);
                    q.add(board);
                }
            }
        }
    ;    return 0;
    }

    static class Board{
        int emo;
        int clipboard;
        int time;

        public Board(int emo, int clipboard, int time) {
            this.emo = emo;
            this.clipboard = clipboard;
            this.time = time;
        }

        @Override
        public boolean equals(Object o){
            if(this == o) return true;
            if(o == null || getClass() != o.getClass()) return false;
            Board board = (Board) o;
            return emo == board.emo && clipboard == board.clipboard && time == board.time;
        }

        @Override
        public int hashCode(){
            return Objects.hash(emo, clipboard, time);
        }

    }
}
