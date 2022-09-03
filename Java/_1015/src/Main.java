import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }
        System.out.println(solution(n, m, map));
    }

    private static int solution(int n, int m, int[][] map) {
        int maxGap = Math.min(n, m);

        for (int gap = maxGap; gap >= 1; gap--) {
            for (int i = 0; i < n - gap; i++) {
                for (int j = 0; j < m - gap; j++) {
                    if(map[i][j] == map[i +  gap][j + gap] 
                            && map[i][j] == map[i][j + gap]
                            && map[i][j] == map[i + gap][j]
                    ){
                        return (gap + 1) * (gap + 1);
                    }
                }
            }
        }
        return 1;
    }
}