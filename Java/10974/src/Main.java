import java.util.ArrayList;
import java.util.NavigableMap;
import java.util.Scanner;

public class Main {
    private static int N;
    private static boolean visited[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        visited = new boolean[N + 1];
        backTracking(new ArrayList<>());
    }

    public static void backTracking(ArrayList<Integer> ary){
        if(ary.size() == N){
            printAry(ary);
            return;
        }
        for(int i = 1; i <= N; i ++){
            if (!visited[i]) {
                ary.add(i);
                visited[i] = true;
                backTracking(ary);
                ary.remove(ary.size() - 1);
                visited[i] = false;
            }
        }
    }

    public static void printAry(ArrayList<Integer> ary){
        for(int i: ary){
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
