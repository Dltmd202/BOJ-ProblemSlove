import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();

        while (true){
            int N = Integer.parseInt(br.readLine());

            if(N == 0) break;

            Solution solution = new Solution(N);
            solution.getData();
            sb.append(solution.solution()).append("\n");
        }
        System.out.println(sb.toString().trim());
    }

    static class Solution{
        int N;
        List<Node> map;

        public Solution(int n) {
            N = n;
            map = new ArrayList<>();
        }

        public void getData() throws IOException {
            Node start = new Node('E', 0);
            start.ways.add(1);
            map.add(start);

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                char type = st.nextToken().charAt(0);
                int cost = Integer.parseInt(st.nextToken());

                Node node = new Node(type, cost);

                while (st.hasMoreTokens()){
                    int next = Integer.parseInt(st.nextToken());

                    if(next == 0) break;

                    node.ways.add(next);
                }
                map.add(node);
            }
        }

        public String solution(){
            int[] visited = new int[N + 1];
            Queue<int[]> q = new ArrayDeque<>();

            q.offer(new int[]{0, 0});
            visited[0] = 0;
            Arrays.fill(visited, -1);

            while (!q.isEmpty()){
                int[] cur = q.poll();
                int curRoomNumber = cur[0];
                int curCost = cur[1];
//                System.out.println(curRoomNumber);
//                System.out.println(curCost);

                if(curRoomNumber == N) return "Yes";

                for (Integer nextRoom : map.get(curRoomNumber).ways) {
                    Node nextNode = map.get(nextRoom);
//                    System.out.print(nextRoom + " ");
//                    System.out.print(nextNode.type + " ");
//                    System.out.println(nextNode.cost);

                    if(visited[nextRoom] >= curCost) continue;
                    if(nextNode.type == 'L'){
                        int nCost = Math.max(curCost, nextNode.cost);
                        q.add(new int[]{nextRoom, nCost});
                        visited[nextRoom] = nCost;
                    } else if(nextNode.type == 'T' && nextNode.cost <= curCost){
                        int nCost = curCost - nextNode.cost;
                        q.add(new int[]{nextRoom, nCost});
                        visited[nextRoom] = nCost;
                    } else if(nextNode.type == 'E'){
                        q.add(new int[]{nextRoom, curCost});
                        visited[nextRoom] = curCost;
                    }
                }
            }

            return "No";
        }

        static class Node {
            char type;
            int cost;
            List<Integer> ways;

            public Node(char type, int cost) {
                this.type = type;
                this.cost = cost;
                ways = new ArrayList<>();
            }

            @Override
            public String
            toString() {
                return "Node{" +
                        "type=" + type +
                        ", cost=" + cost +
                        ", ways=" + ways +
                        '}';
            }
        }
    }
}