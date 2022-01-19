import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    private static final int TABLE_SIZE = 2 * 1_000_001;
    private static Scanner sc = new Scanner(System.in);
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();
    private static boolean[] primeTable;
    private static ArrayList<Integer> primeNumbers;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        primeTable = new boolean[TABLE_SIZE];
        primeNumbers = new ArrayList<>();

        Arrays.fill(primeTable, true);
        setPrimeTable();
        for(int tc = 0; tc < T; tc ++){
            st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());
            solution(a, b);
        }
        System.out.println(sb.toString());
    }

    public static void solution(long a, long b) throws IOException {
        if(a + b >= 4) {
            if ((a + b) % 2 == 0)
                sb.append("YES").append("\n");
            else if (isPrimeNumber(a + b - 2))
                sb.append("YES").append("\n");
            else
                sb.append("NO").append("\n");
        } else
            sb.append("NO").append("\n");
    }

    public static void setPrimeTable(){
        primeTable[0] = false;
        primeTable[1] = false;
        for(int i = 2; i < TABLE_SIZE; i ++){
            int j = 2;
            while(i * j < TABLE_SIZE){
                primeTable[i * j] = false;
                j ++;
            }
        }
        for(int i = 2; i < TABLE_SIZE; i ++){
            if(primeTable[i]) primeNumbers.add(i);
        }
    }

    public static boolean isPrimeNumber(long x){
        if(x < TABLE_SIZE){
            return primeTable[(int) x];
        } else {
            for(int primeNumber: primeNumbers){
                if(x % primeNumber == 0) return false;
            }
        }
        return true;
    }

}