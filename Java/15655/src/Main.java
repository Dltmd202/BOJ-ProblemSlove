import java.util.*;

public class Main {
    private static int N;
    private static int M;
    private static int[] ary;
    private static Map<Integer, Boolean> visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        ary = new int[N];
        visited = new HashMap<>();

        for(int i = 0; i < N; i ++){
            ary[i] = sc.nextInt();
            if(!visited.containsKey(ary[i])){
                visited.put(ary[i], false);
            }
        }
        Arrays.sort(ary);
        getPermutations(new ArrayList<>(), 0);
    }

    public static void getPermutations(ArrayList<Integer> list, int idx){
        if(list.size() == M){
            for(int i: list){
                System.out.print(i + " ");
            }
            System.out.println();
            return;
        }
        for(int i = idx; i < N; i ++){
            if(!visited.get(ary[i])){
                visited.put(ary[i], true);
                list.add(ary[i]);

                getPermutations(list, i + 1);

                visited.put(ary[i], false);
                list.remove(list.size() - 1);
            }
        }
    }
}
