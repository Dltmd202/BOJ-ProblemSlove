import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();
        long sum = 0;
        int numberDigit = 1;


        while (N > (long)Math.pow(10.0, numberDigit) - (long)Math.pow(10.0, numberDigit - 1)){
            sum += ((long)Math.pow(10.0, numberDigit) - (long)Math.pow(10.0, numberDigit - 1)) * numberDigit;
            N -= (((long) Math.pow(10.0, numberDigit)) - (long) Math.pow(10.0, numberDigit - 1));
            numberDigit++;
        }

        sum += (N % (long)Math.pow(10.0, numberDigit)) * numberDigit;

        System.out.println(sum);
    }
}