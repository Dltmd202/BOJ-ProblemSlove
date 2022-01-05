import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    private static int k;
    private static String[] marks;
    private static long max = Long.MIN_VALUE;
    private static long min = Long.MAX_VALUE;
    private static String maxString = String.valueOf(max);
    private static String minString = String.valueOf(min);
    private static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        k = sc.nextInt();
        marks = new String[k];
        visited = new boolean[10];
        for(int i = 0; i < k; i ++){
            marks[i] = sc.next();
        }
        backTracking(new ArrayList<>());
        System.out.println(maxString);
        System.out.println(minString);
    }

    public static void backTracking(ArrayList<Integer> numbers){
        if(numbers.size() == k + 1){
            String res = "";
            for(int number: numbers){
                res += number;
            }
            long current = Long.parseLong(res);
            if(max < current){
                max = current;
                maxString = res;
            }
            if(min > current){
                min = current;
                minString = res;
            }
        } else if(numbers.size() == 0){
            for(int i = 0; i < 10; i ++){
                visited[i] = true;
                numbers.add(i);

                backTracking(numbers);

                visited[i] = false;
                numbers.remove(numbers.size() - 1);
            }
        } else {
            int previous = numbers.get(numbers.size() - 1);
            if(marks[numbers.size() - 1].equals(">")){
                for(int i = previous - 1; i >= 0; i --){
                    if(!visited[i]){
                        visited[i] = true;
                        numbers.add(i);

                        backTracking(numbers);

                        visited[i] = false;
                        numbers.remove(numbers.size() - 1);
                    }
                }
            } else {
                for(int i = previous + 1; i < 10; i ++){
                    if(!visited[i]){
                        visited[i] = true;
                        numbers.add(i);

                        backTracking(numbers);

                        visited[i] = false;
                        numbers.remove(numbers.size() - 1);
                    }
                }
            }
        }
    }
}
