import java.util.*;

public class Main {
    static char[] operator = new char[]{'*', '+', '-', '/'};

    static Calculate[] calculates = new Calculate[]{
            (s) -> s * s,
            (s) -> s + s,
            (s) -> s - s,
            (s) -> s / s
    };
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long s = sc.nextLong();
        long t = sc.nextLong();

        System.out.println(solution(s, t));
    }

    private static String solution(long s, long t) {
        if(s == t) return "0";

        Queue<Node> q = new ArrayDeque<>();
        Set<Long> visited = new HashSet<>();

        q.offer(new Node(s, ""));
        visited.add(s);


        String res = null;

        while (!q.isEmpty()){
            Node cur = q.poll();

            if(cur.res == t){
                return cur.procedure;
            }

            for (int i = 0; i < 4; i++) {
                if(i == 3 && cur.res == 0) continue;
                long ns = calculates[i].calculate(cur.res);
                if(!visited.contains(ns) && ns <= t){
                    q.offer(new Node(ns, cur.procedure + operator[i]));
                    visited.add(ns);
                }
            }

        }
        return "-1";
    }

    static class Node{
        long res;
        String procedure;

        public Node(long res, String procedure) {
            this.res = res;
            this.procedure = procedure;
        }
    }

    static interface Calculate{
        long calculate(long s);
    }
}