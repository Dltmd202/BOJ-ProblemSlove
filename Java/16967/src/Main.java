import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        int BX = H+X, BY = W+Y;
        int[][] B = new int[BX][BY];
        for(int i =0; i< BX; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j< BY; j++) {
                B[i][j]= Integer.parseInt(st.nextToken());
            }
        }
        int[][] A = new int[H][W];
        for(int i =0; i< BX; i++) {
            for(int j =0; j< BY; j++) {
                if(i<X && j< W) {
                    A[i][j] = B[i][j];
                }else if(j<Y && i<H) {
                    A[i][j] = B[i][j];
                }else if(j>=Y && i>=X  && j< W && i<H) {
                    A[i][j] = B[i][j]-A[i-X][j-Y];
                }
            }
        }

        for(int i =0; i< H; i++) {
            for(int j =0; j< W; j++) {
                System.out.print(A[i][j]+ " ");
            }
            System.out.println();
        }
    }
}