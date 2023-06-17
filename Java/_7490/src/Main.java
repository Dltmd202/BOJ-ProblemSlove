import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    static String[] choice = {" ", "+", "-"};
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        while (T-->0){
            int N = sc.nextInt();
            int opCnt = N - 1;
            List<String> list = new ArrayList<>();

            for (int i = 1; i <= N; i++) {
                list.add(String.valueOf(i));
                list.add(" ");
            }

            search(list, opCnt, 0);
            sb.append("\n");
        }
        System.out.println(sb.toString().trim());
    }

    static void search(List<String> list, int opCnt, int depth){
        if(depth == opCnt){
            String row = list.stream().collect(Collectors.joining());
            String res = row.replace(" ", "");
            StringTokenizer st = new StringTokenizer(res, "[+-]", true);

            long cur = Long.parseLong(st.nextToken());
            int idx = 1;
            while (st.hasMoreTokens()){
                String operator = st.nextToken();
                long right = Long.parseLong(st.nextToken());
                if(operator.equals("+")) cur += right;
                else cur -= right;
            }

            if(cur == 0) sb.append(row.trim()).append("\n");


            return;
        }


        list.set(1 + 2 * depth, choice[0]);
        search(list, opCnt, depth + 1);
        list.set(1 + 2 * depth, choice[1]);
        search(list, opCnt, depth + 1);
        list.set(1 + 2 * depth, choice[2]);
        search(list, opCnt, depth + 1);

    }
}