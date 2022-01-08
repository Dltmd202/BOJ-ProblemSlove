import java.util.Scanner;

public class Main {
    enum Control{
        UP,
        DOWN,
        LEFT,
        RIGHT
    }

    private static final int MAX_MOVE = 5;

    private static int N;
    private static int[][] map;
    private static int answer = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        map = new int[N][N];
        for(int i = 0; i < N; i ++){
            for(int j = 0; j < N; j ++){
                map[i][j] = sc.nextInt();
                answer = Math.max(answer, map[i][j]);
            }
        }
        play2048(map,0);
        System.out.println(answer);
    }

    private static void mapControl(int[][] controlMap, Control direction){
        if(direction == Control.UP){
            for(int j = 0; j < N; j ++){
                int idx = 0;
                int val = 0;
                for(int i = 0; i < N; i ++){
                    if(controlMap[i][j] != 0){
                        if(controlMap[i][j] == val){
                            controlMap[idx - 1][j] = val * 2;
                            answer = Math.max(answer, val * 2);
                            controlMap[i][j] = 0;
                            val = 0;
                        } else {
                            val = controlMap[i][j];
                            controlMap[i][j] = 0;
                            controlMap[idx][j] = val;
                            idx ++;
                        }
                    }
                }
            }
        } else if (direction == Control.DOWN){
            for(int j = 0; j < N; j ++){
                int idx = N - 1;
                int val = 0;
                for(int i = N - 1; i >= 0; i --){
                    if(controlMap[i][j] != 0){
                        if(controlMap[i][j] == val){
                            controlMap[idx + 1][j] = val * 2;
                            answer = Math.max(answer, val * 2);
                            controlMap[i][j] = 0;
                            val = 0;
                        } else {
                            val = controlMap[i][j];
                            controlMap[i][j] = 0;
                            controlMap[idx][j] = val;
                            idx --;
                        }
                    }
                }
            }
        } else if (direction == Control.LEFT){
            for(int i = 0; i < N; i ++){
                int idx = 0;
                int val = 0;
                for(int j = 0; j < N; j ++){
                    if(controlMap[i][j] != 0){
                        if(controlMap[i][j] == val){
                            controlMap[i][idx - 1] = val * 2;
                            answer = Math.max(answer, val * 2);
                            val = 0;
                            controlMap[i][j] = 0;
                        } else {
                            val = controlMap[i][j];
                            controlMap[i][j] = 0;
                            controlMap[i][idx] = val;
                            idx ++;
                        }
                    }
                }
            }
        } else if (direction == Control.RIGHT){
            for(int i = 0; i < N; i ++){
                int idx = N - 1;
                int val = 0;
                for(int j = N - 1; j >= 0; j --){
                    if(controlMap[i][j] != 0){
                        if(controlMap[i][j] == val){
                            controlMap[i][idx + 1] = val * 2;
                            answer = Math.max(answer, val * 2);
                            val = 0;
                            controlMap[i][j] = 0;
                        } else {
                            val = controlMap[i][j];
                            controlMap[i][j] = 0;
                            controlMap[i][idx] = val;
                            idx --;
                        }
                    }
                }
            }
        }
    }

    private static int[][] copyMap(int[][] origin){
        int[][] instance = new int[N][N];
        for(int i = 0; i < N; i ++){
            for(int j = 0; j < N; j ++){
                instance[i][j] = origin[i][j];
            }
        }
        return instance;
    }

    private static void play2048(int[][] gameMap,int cnt){
        if(cnt < MAX_MOVE){
            for(Control control: Control.values()){
                int[][] clonedMap = copyMap(gameMap);
                mapControl(clonedMap, control);
                play2048(clonedMap,cnt + 1);
            }
        }
    }
}
