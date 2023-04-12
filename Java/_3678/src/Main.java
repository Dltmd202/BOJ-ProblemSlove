import java.io.*;
import java.util.Arrays;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        long[] minDp = new long[101];
        String[] maxDp = new String[101];

        Arrays.fill(minDp, Long.MAX_VALUE);
        minDp[2] = 1;
        minDp[3] = 7;
        minDp[4] = 4;
        minDp[5] = 2;
        minDp[6] = 6;
        minDp[7] = 8;
        minDp[8] = 10;

        String[] add = {"1", "7", "4", "2", "0", "8"};

        for (int i = 9; i <= 100; i++) {
            for (int j = 2; j <= 7; j++) {
                String line = minDp[i - j] + add[j - 2];
                minDp[i] = Math.min(Long.parseLong(line), minDp[i]);
            }
        }

        String[] add2 = {"0", "0", "1", "7", "4", "2", "6", "8"};
        maxDp[2] = "1";

        for (int i = 3; i <= 100; i++) {
            String line = "";
            if(i % 2 == 0){
                for (int j = 0; j < i / 2; j++) {
                    line += "1";
                }
            } else {
                int val = i / 2 - 1;
                for (int j = 0; j < val; j++) {
                    line += "1";
                }
                line = add2[i - (val * 2)] + "" + line;
            }
            maxDp[i] = line;
        }

        for(int i=0;i<N;i++) {
            int d = Integer.parseInt(br.readLine());
            System.out.println(minDp[d]+" "+maxDp[d]);
        }







    }
}
