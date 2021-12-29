import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static int pivot;
    private static int step;
    private static int N;
    private static int L;
    private static List<Integer> answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        L = sc.nextInt();
        answer = new ArrayList<>();
        if(solution()){
            for(int ans: answer){
                System.out.print(ans + " ");
            }
        } else {
            System.out.println(-1);
        }
    }

    public static boolean solution(){
        for(step = L; step <= 100; step ++){
            pivot = N / step - ((step % 2 == 0) ? step / 2 - 1: step / 2);
            int res = rangeSum(pivot, pivot + step);
            if (pivot < 0) return false;
            if (res == N){
                for(int i = pivot; i < pivot + step; i ++) {
                    answer.add(i);
                }
                return true;
            }
        }
        return false;
    }

    public static int rangeSum(int i, int j){
        int res = 0;
        for(; i < j; i ++) {
            res += i;
        }
        return res;
    }
}
