import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Map<Integer, Integer> coordinate = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        int answer = 0;

        int n = sc.nextInt();
        int l = sc.nextInt();
        int[] ends = new int[n];
        for (int i = 0; i < n; i ++){
            int start = sc.nextInt();
            int end = sc.nextInt();
            ends[i] = end;
            coordinate.put(end, start);
        }
        Arrays.sort(ends);
        int cur = 0;
        for (int i = 0; i < n; i ++){
            int end = ends[i];
            int start = coordinate.get(end);
            int dif = end - Math.max(start, cur);
            int stick = (int)(Math.ceil((double) dif / l));
            cur = Math.max(start, cur) + (stick * l);
            answer += stick;
        }
        System.out.println(answer);
    }
}
