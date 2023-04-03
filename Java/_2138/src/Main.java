import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String now = sc.next();
        String expect = sc.next();

        int[] first = new int[n];
        int[] second = new int[n];
        int[] expected = new int[n];

        for(int i = 0; i < n; i++) {
            first[i] = now.charAt(i)-'0';
            second[i] = now.charAt(i)-'0';
            expected[i] = expect.charAt(i)-'0';
        }

        first[0] = toggle(first[0]);
        first[1] = toggle(first[1]);


        int res1 = solution(n, 1, first, expected);
        int res2 = solution(n, 0, second, expected);



        if(res1 == Integer.MAX_VALUE && res2 == Integer.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(Math.min(res1, res2));
    }

    private static int solution(int n, int res, int[] current, int[] expected) {
        for(int i = 1; i < n; i++) {
            if(current[i - 1] != expected[i - 1]) {
                current[i - 1] = toggle(current[i - 1]);
                current[i] = toggle(current[i]);
                res++;

                if(i != n - 1)
                    current[i + 1] = toggle(current[i + 1]);
            }
        }

        return current[n - 1] != expected[n - 1] ? Integer.MAX_VALUE : res;
    }

    public static int toggle(int light){
        return 1 - light;
    }
}
