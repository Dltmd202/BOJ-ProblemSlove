import java.io.*;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
	// write your code here
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        HashSet<Integer> cards = new HashSet<>();

        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i ++) {
            int card = Integer.parseInt(st.nextToken());
            cards.add(card);
        }
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int[] res = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i ++) {
            int card = Integer.parseInt(st.nextToken());
            if (cards.contains(card)) {
                res[i] = 1;
            } else {
                res[i] = 0;
            }
        }
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < m; i ++){
            sb.append(res[i]).append(" ");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}
