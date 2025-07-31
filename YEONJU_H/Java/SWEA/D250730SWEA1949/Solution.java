package D250730SWEA1949;

import java.util.*;
import java.io.*;


public class Solution {

    static int[][] map;
    static int[] dr = {0,0,1,-1};
    static int[] dc = {1,-1,0,0};
    static int N,K,highestH, maxDis;

    public static void main(String[] args) throws IOException {
        /*
            등산로 만드는 규칙
            1) 가장 높은 봉우리에서 시작
            2) 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결되어야 함
               - 높이가 같은 곳 혹은 낮은 지형
               - 대각선 방향의 연결은 불가능
            3) 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깍는 공사 가능

            N = 지도의 가로 세로
            K = 최대 공사 가능 깊이

            3 <= 한 변의 길이 <= 8
            1 <= 최대 공사 가능 깊이 <= 5
            1 <= 지형의 높이 <= 20
            가장 높은 봉오리 : 최대 5개

            [ 출력 ]
            만들 수 있는 가장 긴 등산로의 기리

            [ 아이디어 ]
            1) 가장 높은 봉우리를 찾아 그 위치와 숫자를 기억한다.
            2) 각각의 봉우리에서 시작해서, 낮은 곳을 찾아 내려간다. (방문 처리 필수)
            - 각 노드별로 방문처리 배열을 따로 가져가야 함
            - 더 이상 주변에 더 낮은 자리가 없고, 움직인 거리가 다른 봉우리보다 길 때만 거리 저장
            - BFS 사용 -> DFS와 백트래킹 응용
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int t = 0;

        while(t++ < T) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            map = new int[N][N];
            highestH = 0;

            boolean[][] V = new boolean[N][N];
            int dis = 0;
            boolean isDug = false;

            for(int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                    if(map[i][j] > highestH) {
                        highestH = map[i][j];
                    }
                }
            }

//            System.out.println(Arrays.deepToString(map));
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(map[i][j] == highestH) {
                        V[i][j] = true;
                        hikingDown(i,j,V,dis,isDug);
                    }
                }
            }
        }

    }

    static void hikingDown(int r, int c, boolean[][] V, int dis, boolean isDug) {

        for(int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(nr < N && nc < N && nr >= 0 && nc >= 0) {
                // 아래 쪽으로 내려가는 것을 찾아서 땅을 파지 않을 경우
                if(map[nr][nc] < map[r][c] && !V[nr][nc]) {
                    V[nr][nc] = true;
                    hikingDown(nr,nc,V,dis + 1, isDug);
                    V[nr][nc] = false;
                }

                // 땅을 팔 경우
                if(map[nr][nc] > map[r][c] && map[nr][nc] - K < map[r][c] && !V[nr][nc] && !isDug) {
                    V[nr][nc] = true;
                    map[nr][nc] = map[nr][nc] - K;
                    isDug = true;
                    hikingDown(nr,nc,V,dis + 1, isDug);
                    map[nr][nc] = map[nr][nc] + K;
                    V[nr][nc] = false;
                }
                // 가지도, 땅파지도 않을 경우 -> 아무일도 안일어남
            }
        }

        // 네 방향 다 살펴도 더 이상 갈 곳이 없을 경우 stop
        maxDis = Math.max(maxDis, dis);

    }

}
