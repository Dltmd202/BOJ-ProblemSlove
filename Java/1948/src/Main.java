import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static List<Bridge>[] graph;
    static List<Bridge>[] reverseGraph;
    static boolean[] passingVisit;
    static int passCnt;
    static int[] ind;
    static int[] time;
    static int N;
    static int M;
    static int firstDeparture;
    static int finalArrive;

    public static void main(String[] args) throws IOException{
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        graph = new ArrayList[N + 1];
        reverseGraph = new ArrayList[N + 1];
        ind = new int[N + 1];
        time = new int[N + 1];
        passingVisit = new boolean[N + 1];

        for (int i = 1; i < N + 1; i ++){
            graph[i] = new ArrayList<>();
            reverseGraph[i] = new ArrayList<>();
        }

        StringTokenizer st;
        for(int i = 0; i < M; i ++){
            st = new StringTokenizer(br.readLine());
            int depart = Integer.parseInt(st.nextToken());
            int arrive = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());

            ind[arrive] += 1;
            graph[depart].add(new Bridge(depart, arrive, time));
            reverseGraph[arrive].add(new Bridge(arrive, depart, time));
        }
        st = new StringTokenizer(br.readLine());
        firstDeparture = Integer.parseInt(st.nextToken());
        finalArrive = Integer.parseInt(st.nextToken());

        makeTimeTable();
        searchPassThrough(finalArrive);
        System.out.println(time[finalArrive]);
        System.out.println(passCnt);
    }

    static void makeTimeTable(){
        Queue<Integer> q = new LinkedList<>();
        q.offer(firstDeparture);

        while(!q.isEmpty()){
            int now = q.poll();

            for(Bridge will: graph[now]){
                ind[will.arrive] -= 1;
                time[will.arrive] = Math.max(
                        time[will.arrive],
                        time[now] + will.time);
                if(ind[will.arrive] == 0){
                    q.offer(will.arrive);
                }
            }
        }
    }

    static void searchPassThrough(int start){
        if(passingVisit[start]) return;
        passingVisit[start] = true;

        for(Bridge will : reverseGraph[start]){
            if(time[start] == time[will.arrive] + will.time){
                passCnt++;
                searchPassThrough(will.arrive);
            }
        }
    }

    static class Bridge{
        int depart;
        int arrive;
        int time;

        public Bridge(int depart, int arrive, int time){
            this.depart = depart;
            this.arrive = arrive;
            this.time = time;
        }
    }
}
