import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[] operatorCounts;
    private static int[] data;
    private static int max = Integer.MIN_VALUE;
    private static int min = Integer.MAX_VALUE;
    private static Calculator[] calculators = new Calculator[] {
            (a, b) -> a + b,
            (a, b) -> a - b,
            (a, b) -> a * b,
            (a, b) -> a / b
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        data = new int[N];
        operatorCounts = new int[4];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            operatorCounts[i] = Integer.parseInt(st.nextToken());
        }

        search(new ArrayList<>());
        System.out.println(max);
        System.out.println(min);
    }

    public static void search(List<Integer> operators){
        if(N - 1 == operators.size()){
            int res = data[0];
            for (int i = 1; i < N; i++) {
                int operator = operators.get(i - 1);
                res = calculators[operator].calculate(res, data[i]);
            }
            min = Math.min(res, min);
            max = Math.max(res, max);
            return;
        }

        for (int operator = 0; operator < 4; operator++) {
            int operatorCount = operatorCounts[operator];
            if(operatorCount == 0) continue;

            operators.add(operator);
            operatorCounts[operator]--;
            search(operators);

            operators.remove(operators.size() - 1);
            operatorCounts[operator]++;
        }
    }

    static interface Calculator{
        int calculate(int a, int b);
    }
}
