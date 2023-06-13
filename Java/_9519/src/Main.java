import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[] chars = br.readLine().toCharArray();
        List<String> answer = new ArrayList<>();
        Set<String> visited = new HashSet<>();

        for (int i = 0; i < N; i++) {
            char[] tmp = new char[chars.length];
            List<Character> list = new ArrayList<>();

            int idx = 0;
            for (int j = 0; j < chars.length; j += 2) {
                tmp[idx++] = chars[j];
            }

            idx = chars.length - 1;
            for (int j = 1; j < chars.length; j += 2) {
                tmp[idx--] = chars[j];
            }

            chars = tmp;
            String s = new String(tmp);
            if(!visited.contains(s)) {
                visited.add(s);
                answer.add(new String(tmp));
            } else break;
        }


        System.out.println(answer.get((N + answer.size() - 1) % answer.size()));

    }
}