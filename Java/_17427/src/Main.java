import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long res = 0;

        for (int i = 1; i <= N; i++) {
            res += (i * (N / i));
        }
        System.out.println(res);
    }
}