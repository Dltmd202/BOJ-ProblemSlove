import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    private static Pattern p;
    private static int N;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> strs = new ArrayList<>();
        p = Pattern.compile("(100+1+|01)+");
        N = sc.nextInt();
        Matcher m;
        for(int i = 0; i < N; i ++){
            String str = sc.next().trim();
            m = p.matcher(str);
            if(m.matches()){
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }

    }
}
