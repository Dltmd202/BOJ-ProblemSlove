import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()){
            int n = sc.nextInt();
            long target = 1;
            int length = 1;
            while (target % n != 0){
                target = (target * 10) + 1;
                target %= n;
                length++;
            }
            System.out.println(length);
        }
    }
}