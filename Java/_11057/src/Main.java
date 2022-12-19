import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int M;
    static long[] songs;
    static int curMax;
    static int guitarCnt = -1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        songs = new long[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            char[] mask = st.nextToken().toCharArray();

            for (int j = 0; j < M; j++) {
                if(mask[j] == 'Y')
                    songs[i] = addMask(songs[i], j);
            }
        }

        search(new boolean[N], 0, 0, 0);
        System.out.println(guitarCnt);
    }


    public static void search(boolean[] visited,int idx, long cur, int curGuitarCnt){
        int songCnt = getSongCnt(M, cur);
        if(songCnt > curMax){
            curMax =  songCnt;
            guitarCnt = curGuitarCnt;
        }
        if(songCnt == curMax){
            guitarCnt = Math.min(curGuitarCnt, guitarCnt);
        }

        if(curGuitarCnt >= N) return;

        for (int i = idx; i < songs.length; i++) {
            if(!visited[i]){
                long newMask =  unionMask(cur, songs[i]);
                visited[i] = true;

                search(visited,  i + 1, newMask, curGuitarCnt + 1);
                visited[i] = false;
            }
        }
    }

    public static long addMask(long set, int seq){
        return set | (1L << seq);
    }

    public static long unionMask(long set1, long set2){
        return set1 | set2;
    }

    public static long subMask(long set1, long set2){
        return set1 & (~set2);
    }

    public static boolean isFull(int M, long set){
        return set == ((1L << M) - 1);
    }

    public static int getSongCnt(int M, long set){
        int cnt = 0;
        long tmp = 1;
        while(tmp != (1L << M)){
            if((set & tmp) != 0) cnt++;
            tmp <<= 1;
        }
        return cnt;
    }
}