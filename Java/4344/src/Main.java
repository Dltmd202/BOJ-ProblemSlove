import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int tb = 0 ; tb < t ; tb ++){

            int n = sc.nextInt();
            int[] score = new int[n];
            int aboveAvgCount = 0 ;
            double avg = 0 , sum = 0;

            for (int i = 0 ; i < n ; i ++) {
                score[i] = sc.nextInt();
                sum += score[i];
            }

            avg = sum / n;


            for (int i = 0 ; i < n ; i ++){
                if ( score[i] > avg) {
                    aboveAvgCount += 1;
                }
            }

            System.out.format("%.3f%%\n",(double) aboveAvgCount/n * 100);
        }
    }
}
