import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();

        System.out.println(
                checkAkaPalindrome(S.toCharArray(), 0, S.length() - 1) ? "AKARAKA" : "IPSELENTI"
        );
    }

    public static boolean checkAkaPalindrome(char[] s, int left, int right){
        if(right - left <= 1){
            if(right - left == 0) return true;
            else return s[left] == s[right];
        }

        int mid = (right + left) / 2;


        if((right - left) % 2 == 0){
            boolean leftRes = checkAkaPalindrome(s, left, mid - 1);
            boolean rightRes = checkAkaPalindrome(s, mid + 1, right);
            if(!leftRes & !rightRes) return false;
        } else {
            boolean leftRes = checkAkaPalindrome(s, left, mid);
            boolean rightRes = checkAkaPalindrome(s, mid, right);
            if(!leftRes & !rightRes) return false;
        }

        for (int i = left, j = right; i < j; i++, j--) {
            if(s[i] != s[j]) {
                return false;
            }
        }

        return true;
    }
}