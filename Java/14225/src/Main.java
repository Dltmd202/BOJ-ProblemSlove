import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private static int N;
    private static int[] data;
    private static boolean[] visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        int answer = 1;
        visited = new boolean[100_000 * 20 + 1];

        data = new int[N];
        for(int i = 0; i < N; i ++){
            data[i] = sc.nextInt();
        }

        search(0, 0);
        while(true){
            if(!visited[answer++]){
                System.out.println(answer - 1);
                return;
            }
        }
    }

    private static void search(int cnt, int sum){
        if(cnt == N){
            visited[sum] = true;
        } else {
            search(cnt + 1, sum);
            search(cnt + 1, sum + data[cnt]);
        }
    }
}
