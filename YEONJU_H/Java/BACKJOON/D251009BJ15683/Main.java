package D251009BJ15683;

import java.util.*;
import java.io.*;



public class Main {
    static class CCTV {
        int r, c, type;
        CCTV(int r, int c, int type) {
            this.r = r;
            this.c = c;
            this.type = type;
        }
    }

    static int N,M, minBlindSpot;
    static int[][] office;
    static boolean[][] V;
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};
    static int[][][] dirInfo = {{{0},{1},{2},{3}}, {{0,1},{2,3}}, {{0,3},{1,3},{1,2},{0,2}}, {{0,1,3},{3,1,2},{0,2,1},{2,0,3}},{{0,1,2,3}}};
    static ArrayList<CCTV> cctvList = new ArrayList<>();

    // [카메라번호][경우의 수][방향들]
    public static void main(String[] args) throws IOException {
        /*
            문제 정리

            스타트링크의 사무실은 1*1 크기의 정사각형으로 나누어져있는 N*M 크기의 직사각형
            사무실에는 총 K개의 CCTV, 종류는 5종류
            방향에 해당되는 모든 칸을 감시 가능
            벽은 통과 불가 (사각지대) CCTV 끼리는 통과 가능
            CCTV는 회전 가능, 회전은 항상 90도 방향으로 해야하고, 감시하려고 하는 방향은 가로 또는 세로 방향
            0 빈 칸 / 6 벽 / 1~5 CCTV의 번호

            1 : 한방향 : 방향 4가지
            - 상/하/좌/우
            2 : 반대되는 두 방향 : 방향 2가지
            - 상하 / 좌우
            3 : 직각되는 두 방향 : 방향 4가지
            - 상우 / 우하 / 좌하 / 상좌
            4 : 세방향 : 방향 4가지
            - 상우하 / 우하좌 / 상좌하 / 좌상우
            5 : 네방향 : 방향 1가지
            - 상하좌우

            카메라별 방향에 대한 정보를 담은 배열 상0 하1 좌2 우3
            {{0},{1},{2},{3}}, {{0,1},{2,3}}, {{0,3},{1,3},{1,2},{0,2}}, {{0,1,3},{3,1,2},{0,2,1},{2,0,3}},{{1,2,3,4}}

            [ 입력 ]
            사무실 크기(1 ≤ N, M ≤ 8), 상태, CCTV 정보 (CCTV 개수 <=8)

            [ 출력 ]
            CCTV 방향을 적절히 정하여 사각지대의 최소 크기 구하기

            [ 풀이 설계 ]
            각각의 카메라들을 돌려가면서 보이는 칸이 최대가 되는 칸을 찾는다?
            dfs로 한 방향으로 쭉쭉 가면서 찾는다.
            하지만 다른 카메라와 영역이 겹쳤을 경우는?그럼 다른 방향으로 하는 것이 더 효율적일 수도 있는데?
            부르스포스 방법으로 진행? 어떻게 해야할까?

            [ 시간 복잡도 계산 ]
            부르스포스로 진행 시,
            최악의 경우
            CCTV 방향 경우의 수 4^8 = 65536
            각 경우마다 맵 탐색 8*8 = 64 (이 부분 문제풀면서 좀 더 이해)
            65536 * 64 = 대략 400만
            => 결론, 가능할 듯

            1) 맵 전체를 순회하다 CCTV를 찾는다.
            2) 찾은 CCTV들의 방향을 가지고 조합을 만든다.
            예들 들어, 1,2,3,4,5 번이 있으면
            각 cctv들의 가능한 경우의 idx를 조합해서 다양한 조합을 만든다.
            {
                {0},{1},{2},{3}}, // 1번 : 4가지
                {{0,1},{2,3}},  // 2번 : 2가지
                {{0,3},{1,3},{1,2},{0,2}}, // 3번 : 4가지
                {{0,1,3},{3,1,2},{0,2,1},{2,0,3}}, // 4번 : 4가지
                {{1,2,3,4} // 5번 : 1가지
            }


            조합들을 모두 탐색해서 사각지대를 cnt 한다.
            1,1인덱스면
            2번카메라 2,3 방향 순차 탐색

            만들어지는 조합은 아래 정보를 담고 있어야함
            배열이면서,
            카메라 번호, 해당 카메라의 위치, 방향Idx

         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        office = new int[N][M];
        V = new boolean[N][M];

        for(int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for(int c = 0; c < M; c++) {
                office[r][c] = Integer.parseInt(st.nextToken());

                if(office[r][c] >= 1 && office[r][c] <= 5) {
                    cctvList.add(new CCTV(r,c,office[r][c]));
//                    V[r][c] = true;
                }

                if(office[r][c] == 6) {
                    V[r][c] = true;
                }
            }
        } // 입력

        minBlindSpot = Integer.MAX_VALUE;
        combi(0);

        System.out.println(minBlindSpot);


    }

    static void combi(int idx) {

        if(idx == cctvList.size()) {
//            for(int i = 0; i < V.length; i++) {
//                System.out.println(Arrays.toString(V[i]));
//            }
            // 여기서 현재의 사각지대 체크
            int tmp = checkBlind();
            minBlindSpot = Math.min(minBlindSpot, tmp);
            return;
        }

        CCTV cctv = cctvList.get(idx);
        int camType = cctv.type - 1;
        for(int dirIdx = 0; dirIdx < dirInfo[camType].length; dirIdx++) {
            boolean[][] backup = new boolean[N][M];
            for(int i = 0; i < N; i++) {
                backup[i] = V[i].clone();
            }
            // 현재 설정된 카메라 방향의 하위 방향들 탐색
            checkCamDir(cctv, dirIdx, true);

            combi(idx+1);

            // 복구
            for(int i = 0; i < N; i++) {
                V[i] = backup[i].clone();
            }

            // 다시 되돌리기
//            checkCamDir(cctv, dirIdx, false);
        }

    }

    static int checkBlind() {
        int cntBlind = 0;
        for(int r = 0; r < N; r++) {
            for(int c = 0; c < M; c++) {
                if(office[r][c] == 0 && !V[r][c] ) {
                    cntBlind++;
                }
            }
        }
        return cntBlind;
    }

    // 특정 카메라의 특정 방향으로 화면을 확인하는 메서드
    static void checkCamDir (CCTV cctv, int dirIdx, boolean isCheck) {
        int camNo = cctv.type - 1;
        int camR, camC;
        for(int k = 0; k < dirInfo[camNo][dirIdx].length; k++) {
            camR = cctv.r;
            camC = cctv.c;
            while(true) {
                int nr = camR + dr[dirInfo[camNo][dirIdx][k]];
                int nc = camC + dc[dirInfo[camNo][dirIdx][k]];

                if(nr < 0 || nc < 0 || nr >= N || nc >= M) break; // 범위를 벗어남
                if(office[nr][nc] == 6) break; // 벽을 만남

                V[nr][nc] = isCheck;
                camR = nr;
                camC = nc;
            }

        }
    }
}
