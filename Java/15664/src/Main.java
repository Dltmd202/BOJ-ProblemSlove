import java.util.*;

public class Main {
    private static int N;
    private static int M;
    private static int[] data;
    private static StringBuilder sb;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sb = new StringBuilder();
        N = sc.nextInt();
        M = sc.nextInt();
        data = new int[N];

        for(int i = 0; i < N; i ++){
            data[i] = sc.nextInt();
        }
        Arrays.sort(data);
        backTracking(new ArrayList<>(), 0);

        System.out.println(sb.toString());
    }

    public static void backTracking(ArrayList<Integer> items, int idx){
        if(items.size() == M){
            for(int item: items){
                sb.append(item).append(" ");
            }
            sb.append("\n");
        } else {
            Set<Integer> contains = new HashSet<>();
            for (int i = idx; i < data.length; i++) {
                if(!contains.contains(data[i])) {
                    contains.add(data[i]);
                    items.add(data[i]);
                    backTracking(items, i + 1);
                    items.remove(items.size() - 1);
                }
            }
        }
    }
}
