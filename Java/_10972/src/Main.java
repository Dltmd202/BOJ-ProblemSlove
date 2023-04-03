import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<>();

        int[] data = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        list.add(data[N - 1]);

        boolean res = false;
        for (int i = N - 2; i >= 0; i--) {
            if(data[i] < data[i + 1]){
                res = true;

                Collections.sort(list);

                for (int j = 0; j < list.size(); j++) {
                    if(data[i] < list.get(j)){
                        int temp = list.remove(j);
                        list.add(data[i]);
                        data[i] = temp;
                    }
                }

                Collections.sort(list);


                for (int j = i + 1, k = 0; j < N; j++, k++) {
                    data[j] = list.get(k);
                }

                break;

            } else {
                list.add(data[i]);
            }
        }

        if(res){
            for (int i = 0; i < N; i++) {
                System.out.print(data[i] +  " ");
            }
        } else
            System.out.print(-1);

        System.out.println();
    }
}