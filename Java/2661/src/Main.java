import java.util.Scanner;

public class Main {
    private static int N;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        System.out.println(searchGoodSeq(""));
    }

    private static String searchGoodSeq(String now){
        if(now.length() == N){
            return now;
        } else {
            String ret = "";
            for(int i = 1; i <= 3; i++){
                if(isGoodSeq(now + i)){
                    ret = searchGoodSeq(now + i);
                    if (!ret.equals("")){
                        return ret;
                    }
                }
            }
        }
        return "";
    }

    private static boolean isGoodSeq(String now){
        int len = now.length() / 2;

        for(int i = 1; i <= len; i ++){
            if(now.substring(now.length() - i).
                    equals(now.substring(now.length() - 2 * i, now.length() - i))){
                return false;
            }
        }
        return true;
    }
}
