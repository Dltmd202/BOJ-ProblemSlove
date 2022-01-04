import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;
    private static int M;
    private static int[] data;
    private static StringBuilder sb;
    private static Map<Integer, Boolean> visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        data = new int[N];
        visited = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i ++){
            data[i] = Integer.parseInt(st.nextToken());
            if(!visited.containsKey(data[i])){
                visited.put(data[i], false);
            }
        }
        Arrays.sort(data);
        getPermutations(new ArrayList<>());
        System.out.println(sb);
    }

    public static void getPermutations(ArrayList<Integer> ary){
        if(ary.size() == M){
            for(int i: ary){
                sb.append(i + " ");
            }
            sb.append("\n");
            return;
        }
        for(int i = 0; i < N; i ++) {
            ary.add(data[i]);

            getPermutations(ary);

            ary.remove(ary.size() - 1);
        }
    }
}
