import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int M;
    private static int K;
    private static Ground[][] grounds;
    static int[] dy = {0, 0, -1, 1, 1, 1, -1, -1};
    static int[] dx = {1, -1, 0, 0, 1, -1, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        grounds = new Ground[N][N];
        int answer = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                grounds[i][j] = new Ground();
                grounds[i][j].y = i;
                grounds[i][j].x = j;
                grounds[i][j].addition = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            Tree tree = new Tree();
            tree.y = Integer.parseInt(st.nextToken());
            tree.x = Integer.parseInt(st.nextToken());
            tree.age = Integer.parseInt(st.nextToken());
            tree.x--;
            tree.y--;

            grounds[tree.y][tree.x].trees.add(tree);
        }

//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < N; j++) {
//                System.out.print(grounds[i][j]);
//            }
//            System.out.println();
//        }


        for (int k = 0; k < K; k++) {
            List<Tree> lives = new ArrayList<>();
            List<Tree> deads = new ArrayList<>();
//            System.out.println(k + " **********************");

            // 봄
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    grounds[i][j].trees.sort((t1, t2) -> t1.age - t2.age);
                    List<Tree> groundLiveTrees = new ArrayList<>();

                    for(Tree tree : grounds[i][j].trees){
                        if(grounds[i][j].nut >= tree.age){
                            groundLiveTrees.add(tree);
                            grounds[i][j].nut -= tree.age;
                            tree.age++;
                            lives.add(tree);
                        } else {
                            deads.add(tree);
                        }
                    }

                    grounds[i][j].trees = groundLiveTrees;
                }
            }

//            System.out.println("After Spring");
//            for (int i = 0; i < N; i++) {
//                for (int j = 0; j < N; j++) {
//                    System.out.print(grounds[i][j]);
//                }
//                System.out.println();
//            }

            //여름
            for(Tree tree : deads){
                grounds[tree.y][tree.x].nut += (tree.age / 2);
            }

//            System.out.println("After Summer");
//            for (int i = 0; i < N; i++) {
//                for (int j = 0; j < N; j++) {
//                    System.out.print(grounds[i][j]);
//                }
//                System.out.println();
//            }

            //가을
            int newTreeCnt = 0;
            for (Tree tree : lives){
                if(tree.age % 5 != 0) continue;

                for (int i = 0; i < 8; i++) {
                    int ny = tree.y + dy[i];
                    int nx = tree.x + dx[i];

                    if(0 > ny || ny >= N || 0 > nx || nx >= N) continue;
                    Tree newTree = new Tree();
                    newTree.age = 1;
                    newTree.y = ny;
                    newTree.x = nx;
                    grounds[ny][nx].trees.add(newTree);
                    newTreeCnt++;
                }
            }


            //겨울
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    grounds[i][j].nut += grounds[i][j].addition;
                }
            }

            answer = lives.size() + newTreeCnt;

//            System.out.println("After Winter");
//            for (int i = 0; i < N; i++) {
//                for (int j = 0; j < N; j++) {
//                    System.out.print(grounds[i][j]);
//                }
//                System.out.println();
//            }
        }

        System.out.println(answer);

    }

    static class Ground{
        int y;
        int x;
        List<Tree> trees = new ArrayList<>();
        int nut = 5;
        int addition = 0;

        public String toString(){

            return String.format("[nut=%2d, addition=%2d, trees=%30s] ", nut, addition, trees);
        }
    }

    static class Tree{
        int y;
        int x;
        int age = 1;

        public String toString(){
            return String.format("{%d}", age);
        }
    }
}