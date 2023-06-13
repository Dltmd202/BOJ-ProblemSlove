import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] buttons = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            buttons[i] = Integer.parseInt(st.nextToken());
        }

        int K = Integer.parseInt(br.readLine());

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());

            int gender = Integer.parseInt(st.nextToken());
            int number = Integer.parseInt(st.nextToken());

            if(gender == 1){
                for (int j = number - 1; j < N; j += number) {
                    buttons[j] = buttons[j] == 0 ? 1 : 0;
                }
            } else {
                number -= 1;
                int left = number - 1;
                int right = number + 1;

                buttons[number] = buttons[number] == 0 ? 1 : 0;
                while (0 <= left && right < N && buttons[left] == buttons[right]){
                    buttons[left] = buttons[left] == 0 ? 1 : 0;
                    buttons[right] = buttons[right] == 0 ? 1 : 0;
                    left--;
                    right++;
                }
            }
        }


        for(int i=0; i< N; i++) {
            System.out.print(buttons[i] + " ");
            if( (i+1) % 20 == 0)
                System.out.println();
        }

    }
}