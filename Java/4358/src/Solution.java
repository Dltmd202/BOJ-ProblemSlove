import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {

	    Map<String, Integer>trees = new TreeMap<String, Integer>();
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int totalCnt = 0;

        String tree = br.readLine();
        while (true){
            if(tree == null) break;
            trees.put(tree, trees.getOrDefault(tree, 0) + 1);
            tree = br.readLine();
            totalCnt ++;
        }


        for(String treeKey: trees.keySet()){
            float res = (float)trees.get(treeKey) / totalCnt * 100;
            System.out.format("%s %.4f\n", treeKey, res);
        }

    }
}
