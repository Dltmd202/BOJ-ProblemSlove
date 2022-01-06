import java.util.Scanner;

public class Main {
    private static int N;
    private static int step = 0;
    private static int cur = -1;
    private static long answer = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        while(N > cur){
            step++;
            if(step > 10){
                System.out.println(-1);
                return;
            }
            backTracking("");
        }
        System.out.println(answer);
    }

    public static void backTracking(String now){
        if(now.length() == step){
            if(N == ++ cur){
                answer = Long.parseLong(now);
                return;
            }
        } else {
            for(int i = 0; i < 10; i ++){
                if(now.length() == 0) backTracking(now + i);
                else{
                    if(now.charAt(now.length() - 1) - '0' > i){
                        backTracking(now + i);
                    }
                }
            }
        }

    }
}
