package D250927BJ21922;

import java.io.*;
import java.util.*;
public class Main {

    static int N, M;
    static int[][] lab;
    static Queue<int[]> q = new LinkedList<>();
    static boolean[][] ansV;
    static boolean[][][] V;
    static int[] dr = {-1,1,0,0}; // 상하좌우
    static int[] dc = {0,0,-1,1};

    public static void main (String[] args) throws IOException{

        /*
            학부 연구생 민상

            - 자리 정하기 / 격자모양 연구실
            - 에어컨 바람 상하좌우 4방향
            - 에어컨 위치한 곳에도 바람 붐
            - 에어컨 바람이 지나가는 곳 중 하나를 선택하여 앉으려 함
            - 연구실의 4가지 종류 물건이 바람의 방향을 바꿈
            - 물건과 에어컨 위치 상관없이 모두 앉을 수 있음

            [ 출력 ]
            민상이 원하는 자리가 몇개인지 계산

            [ 조건 ]
            연구실의 크기
            - 세로 1 <= N <= 2000
            - 가로 1 <= M <= 2000

            - 두번째 줄부터 N+1줄까지 연구실 내부 구조 정보를 알려주는 값 M개 주어짐
            - 1,2,3,4는 위에서 설명한 물건 종류
            - 9: 에어컨 / 0 : 빈공간
            - 에어컨은 0개 이상 50개 이하

            [ 풀이 설계 ]
            bfs, dfs
            상하좌우
            최단거리

            물건 1 : 좌->우->좌 / 우->좌->우
            물건 2 : 상->하->상 / 하->상->하
            물건 3 : 왼->우->상 / 우->좌->하
                    상->하->좌 / 하->상->우
            물건 4 : 왼->우->하 / 우->좌->상
                    상->하->우 / 하->상->좌
         */


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = new boolean[N][M][4];
        ansV = new boolean[N][M];
        lab = new int[N][M];
        for(int r = 0 ; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for(int c = 0; c < M; c++) {
                lab[r][c] = Integer.parseInt(st.nextToken());
                if(lab[r][c] == 9) {
                    q.add(new int[]{r,c});
                }
            }
        }

        move();

        int ans = 0;

        for(int r = 0; r < N; r++) {
            for(int c = 0; c < M; c++) {
                for(int k = 0; k < 4; k++) {
                    if(V[r][c][k]) ansV[r][c] = true;
                }
            }
        }

        for(int r = 0; r < N; r++) {
            for(int c = 0; c < M; c++) {
                if(ansV[r][c]){
                    ans++;
                }
            }
        }

        System.out.println(ans);
    }

    public static void move() {

        while(!q.isEmpty()) {
            int[] tmp = q.poll();
            int r = tmp[0];
            int c = tmp[1];
            int dir = 0;
            ansV[r][c] = true;

            int curR, curC;
            curR = r;
            curC = c;

            // 0 상 / 1 하 / 2 좌 / 3 우
            for(int k = 0; k < 4; k++) {
                r = curR;
                c = curC;
                dir = k;
                while(true) {
                    int nr = r + dr[dir];
                    int nc = c + dc[dir];
                    if(nr >= N || nc >= M || nr < 0 || nc < 0) {
                        break;
                    }
                    if(V[nr][nc][dir]) break;
                    V[nr][nc][dir]= true;
                    switch(lab[nr][nc]) {
                        case 1 :
                            if(dir == 2) { // 좌 → 우
                                dir = 3;
                            } else if(dir == 3) { // 우 → 좌
                                dir = 2;
                            }
                            r = nr;
                            c = nc;
                            break;
                        case 2 :
                            if(dir == 0) {
                                dir = 1;
                            } else if(dir == 1) {
                                dir = 0;
                            }
                            r = nr;
                            c = nc;
                            break;
                        case 3 : // 상하좌우
                            if(dir == 0) { // 하상우
                                dir = 3;
                            } else if(dir == 1) {// 상하좌
                                dir = 2;
                            } else if(dir == 2) { // 우좌하
                                dir = 1;
                            } else { // 좌우상
                                dir = 0;
                            }
                            r = nr;
                            c = nc;
                            break;
                        case 4 :
                            if(dir == 0) { //하상좌
                                dir = 2;
                            } else if(dir == 1) {// 상하우
                                dir = 3;
                            } else if(dir == 2) { // 우좌상
                                dir = 0;
                            } else { // 좌우하
                                dir = 1;
                            }
                            r = nr;
                            c = nc;
                            break;
                        default:                             r = nr;
                            c = nc;
                    }

                }

                }
            }

    }
}


