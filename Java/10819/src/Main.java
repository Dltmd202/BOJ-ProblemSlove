import java.security.KeyStore;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private static int N;
    private static int[] array;
    private static boolean[] visited;
    private static int score;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        array = new int[N];
        visited = new boolean[N];
        for(int i = 0; i < N; i ++){
            array[i] = sc.nextInt();
        }
        backTracking(new ArrayList<>());
        System.out.println(score);
    }

    public static void backTracking(ArrayList<Integer> ary){
        if(ary.size() == N){
            score = Math.max(score, getScore(ary));
            return;
        }
        for(int i = 0; i < N; i ++){
            if(!visited[i]){
                visited[i] = true;
                ary.add(array[i]);

                backTracking(ary);

                visited[i] = false;
                ary.remove(ary.size() - 1);
            }
        }
    }

    private static int getScore(ArrayList<Integer> ary) {
        int score = 0;
        for(int i = 0; i < N - 1; i ++){
            score += Math.abs(ary.get(i) - ary.get(i + 1));
        }
        return score;
    }
}
