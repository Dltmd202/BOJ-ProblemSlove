import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static String pattern = "";
    private static StringBuilder sb = new StringBuilder();
    private static String[] answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        answer = new String[N];

        for(char ch: br.readLine().toCharArray()){
            pattern += ch == '*' ? "(.*)": ch;
        }

        for(int i = 0; i < N; i ++){
            answer[i] = br.readLine().matches(pattern) ? "DA": "NE";
        }
        System.out.println(String.join("\n", answer));
    }
}
