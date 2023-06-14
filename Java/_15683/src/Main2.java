import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main2 {
    static int N;
    static int M;
    static int defaultBlind = 0;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][M];
        List<Cctv> cctvs = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());

                if(map[i][j] >= 1 && map[i][j] <= 5)
                    cctvs.add(new Cctv(map[i][j], i, j));
                if(map[i][j] == 0) defaultBlind++;
            }
        }
        answer = defaultBlind;
        search(map, cctvs, new ArrayList<>());
        System.out.println(answer);
    }

    public static void search(int[][] map, List<Cctv> cctvs, List<Integer> directions){
        if(cctvs.size() == directions.size()){
            boolean[][] visited = new boolean[N][M];
            int sum = 0;

            for (int i = 0; i < cctvs.size(); i++) {
                Cctv cur = cctvs.get(i);
                int direction = directions.get(i);

                if(cur.id == 1){
                    if(direction == 0){
                        sum = right(map, visited, sum, cur);
                    } else if(direction == 1){
                        sum = down(map, visited, sum, cur);
                    } else if(direction == 2){
                        sum = left(map, visited, sum, cur);
                    } else if(direction == 3){
                        sum = up(map, visited, sum, cur);
                    }
                } else if(cur.id == 2){
                    if(direction == 0){
                        sum = right(map, visited, sum, cur);
                        sum = left(map, visited, sum, cur);
                    } else if(direction == 1){
                        sum = up(map, visited, sum, cur);
                        sum = down(map, visited, sum, cur);
                    }
                } else if(cur.id == 3){
                    if(direction == 0){
                        sum = up(map, visited, sum, cur);
                        sum = right(map, visited, sum, cur);
                    } else if(direction == 1){
                        sum = right(map, visited, sum, cur);
                        sum = down(map, visited, sum, cur);
                    } else if(direction == 2){
                        sum = down(map, visited, sum, cur);
                        sum = left(map, visited, sum, cur);
                    } else if(direction == 3){
                        sum = left(map, visited, sum, cur);
                        sum = up(map, visited, sum, cur);
                    }
                } else if(cur.id == 4){
                    if(direction == 0){
                        sum = up(map, visited, sum, cur);
                        sum = right(map, visited, sum, cur);
                        sum = left(map, visited, sum, cur);
                    } else if(direction == 1){
                        sum = up(map, visited, sum, cur);
                        sum = right(map, visited, sum, cur);
                        sum = down(map, visited, sum, cur);
                    } else if(direction == 2){
                        sum = right(map, visited, sum, cur);
                        sum = left(map, visited, sum, cur);
                        sum = down(map, visited, sum, cur);
                    } else if(direction == 3){
                        sum = up(map, visited, sum, cur);
                        sum = left(map, visited, sum, cur);
                        sum = down(map, visited, sum, cur);
                    }
                } else if(cur.id == 5){
                    if(direction == 0){
                        sum = up(map, visited, sum, cur);
                        sum = right(map, visited, sum, cur);
                        sum = left(map, visited, sum, cur);
                        sum = down(map, visited, sum, cur);
                    }
                }

            }
            answer = Math.min(answer, defaultBlind - sum);

            return;
        }

        Cctv cur = cctvs.get(directions.size());

        for (int i = 0; i < 4; i++) {
            if(cur.id == 2 && i >= 2) break;
            if(cur.id == 5 && i >= 1) break;
            directions.add(i);
            search(map, cctvs, directions);
            directions.remove(directions.size() - 1);
        }
        return;
    }

    static int right(int[][] map, boolean[][] visited, int sum, Cctv cur){
        for (int nx = cur.x + 1; nx < M; nx++) {
            int ny = cur.y;

            if(map[ny][nx] == 0){
                if(!visited[ny][nx]){
                    visited[ny][nx] = true;
                    sum++;
                }
            } else if(map[ny][nx] == 6)break;
        }

        return sum;
    }

    static int down(int[][] map, boolean[][] visited, int sum, Cctv cur){
        for (int ny = cur.y + 1; ny < N; ny++) {
            int nx = cur.x;

            if(map[ny][nx] == 0){
                if(!visited[ny][nx]){
                    visited[ny][nx] = true;
                    sum++;
                }
            } else if(map[ny][nx] == 6)break;
        }

        return sum;
    }
    static int left(int[][] map, boolean[][] visited, int sum, Cctv cur){
        for (int nx = cur.x - 1; nx >= 0; nx--) {
            int ny = cur.y;

            if(map[ny][nx] == 0){
                if(!visited[ny][nx]){
                    visited[ny][nx] = true;
                    sum++;
                }
            } else if(map[ny][nx] == 6)break;

        }
        return sum;
    }

    static int up(int[][] map, boolean[][] visited, int sum, Cctv cur){
        for (int ny = cur.y - 1; ny >= 0; ny--) {
            int nx = cur.x;

            if(map[ny][nx] == 0){
                if(!visited[ny][nx]){
                    visited[ny][nx] = true;
                    sum++;
                }
            } else if(map[ny][nx] == 6)break;
        }

        return sum;
    }


    static class Cctv{
        int id;
        int y;
        int x;

        Cctv(int id, int y, int x){
            this.id = id;
            this.y = y;
            this.x = x;
        }
    }


}
