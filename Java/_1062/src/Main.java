import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        
        String[] words = new String[n];

        for (int i = 0; i < n; i++) {
            words[i] = br.readLine();
            words[i] = words[i].substring(4, words[i].length() - 4);
        }

        System.out.println(solution(n, k, words));
    }
    
    public static int solution(int n, int k, String[] words){
        if(k < 5) return 0;
        else if(k >= 26) return n;
        
        boolean[] visited = new boolean[26];
        visited[ctoi('a')] = true;
        visited[ctoi('c')] = true;
        visited[ctoi('n')] = true;
        visited[ctoi('i')] = true;
        visited[ctoi('t')] = true;
        
        return search(n, k, words, visited, 0, 0);
    }
    
    public static int search(int n, int k, String[] words, boolean[] visited,int ch, int cnt){
        if(cnt == k - 5){
            int count = 0;
            int res = 0;
            for (int i = 0; i < n; i++) {
                count++;
                for (int j = 0; j < words[i].length(); j++) {
                    if(!visited[ctoi(words[i].charAt(j))]){
                        count--;
                        break;
                    }
                }
            }
            res = Math.max(res, count);
            return res;
        }
        
        int ret = 0;
        for (int i = ch; i < 26; i++) {
            if(!visited[i]){
                visited[i] = true;
                ret = Math.max(search(n, k, words, visited, i, cnt + 1), ret);
                visited[i] = false;
            }
        }
        return ret;
    }
    
    public static int ctoi(char x){
        return x - 'a';
    }
}