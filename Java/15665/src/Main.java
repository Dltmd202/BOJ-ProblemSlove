import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    private static int N;
    private static int M;
    static Set<Integer> data = new HashSet<>();
    private static StringBuilder sb;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sb = new StringBuilder();
        N = sc.nextInt();
        M = sc.nextInt();

        for(int i = 0; i < N; i ++){
            data.add(sc.nextInt());
        }
        backTracking(new ArrayList<>());
        System.out.println(sb.toString());
    }

    private static void backTracking(ArrayList<Integer> items){
        if(items.size() == M){
            for(int i: items){
                sb.append(i).append(" ");
            }
            sb.append("\n");
        } else {
            for(int i: data){
                items.add(i);
                backTracking(items);
                items.remove(items.size() - 1);
            }
        }
    }
}
