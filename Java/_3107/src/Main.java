import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String address = br.readLine();

        int i = address.indexOf("::");
        String full = getFullAddress(address);

        StringTokenizer st = new StringTokenizer(full, ":");
        StringBuilder sb = new StringBuilder();

        for (int j = 0; j < 8; j++) {
            String s = st.nextToken();
            int compressed = 4 - s.length();

            sb.append("0".repeat(compressed));
            sb.append(s);

            if(j + 1 < 8) sb.append(":");

        }
        System.out.println(sb.toString());

    }

    public static String getFullAddress(String str){
        int i = str.indexOf("::");
        if(i == -1) return str;

        String prev = str.substring(0, i);
        String post = str.substring(i + 2, str.length());


        StringTokenizer st = new StringTokenizer(prev, ":");

        int prevCnt = 0;
        int postCnt = 0;

        while (st.hasMoreTokens()) {
            prevCnt++;
            st.nextToken();
        }

        st = new StringTokenizer(post, ":");

        while (st.hasMoreTokens()){
            postCnt++;
            st.nextToken();
        }

        int compressed = 8 - (prevCnt + postCnt);

        StringBuilder sb = new StringBuilder();
        if(!prev.equals(""))
            sb.append(prev).append(":");

        for (int j = 0; j < compressed; j++) {
            sb.append("0000");

            if(j + 1 < compressed) sb.append(":");
        }

        if(!post.equals(""))
            sb.append(":").append(post);

        return sb.toString();
    }
}