package D250726SWEA2112;

import java.io.*;
import java.util.*;

public class Solution {
    static int[][] film;
    static int D,W,K,minNum;
    public static void main(String[] args) throws IOException {
        /*
            [ 문제 요약 ]
            단면의 모든 세로방향에 대해 동일한 특성의 셀들이 K개 이상 연속되어야 성능검사 통과
            약품은 막 별로 투입 가능 / 투입하는 막의 모든 셀들은 하나의 특성으로 변경 (가로 방향)
            특성 A = 0 , 특성 B = 1
            D = 보호 필름의 두께
            W = 필름의 가로 크기
            K = 합격 기준

            [ 구해야할 것 ]
            성능 검사 통과를 위한 최소 약품 투입 횟수

            [ 아이디어 ]
            1) 약물 투입 횟수를 늘리고, 조합으로 약물 투입 선택지를 바꿔가면서, 통과 시점 체크
            - 횟수 증가시면서 약물 주입 함수, 막 통과 여부 체크 함수
            2) 통과 되는 순간 return

        */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int t = 0;

        while (t++ < T) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            D = Integer.parseInt(st.nextToken()); // 두께
            W = Integer.parseInt(st.nextToken()); // 가로
            K = Integer.parseInt(st.nextToken());

            film = new int[D][W];
            minNum = 0;

            for(int r = 0; r < D; r++) {
                st = new StringTokenizer(br.readLine());
                for(int c = 0; c < W; c++) {
                    film[r][c] = Integer.parseInt(st.nextToken());
                }
            }

//            System.out.println(Arrays.deepToString(film));
            injection();

            System.out.println("#" + t + " " + minNum);
        }

    }

    static public void injection() {
        int injectNum = 0;

        if(checkFilm(film)) { // 이미 합격 필름이면 return
            return;
        }

        while(injectNum <= D) { // 인젝션 수를 늘려가면서, 조합 만들기
            injectNum++;
            if(injectSimulate(0, injectNum, 0)) {
                minNum = injectNum;
                return;
            }
        }

    }

    static public boolean injectSimulate(int row, int injectNum, int useNum) {

        if(useNum == injectNum) {
            return checkFilm(film);
        }

        if(row >= D) return false; // 더 이상 선택할 막이 없음

        // 현재 막을 선택하지 않는 경우
        if(injectSimulate(row + 1, injectNum, useNum)) {
            return true;
        }

        // 한줄을 모두 A로? 한줄을 모드 B로? 두 방법도 달리해야..
        // 몇줄을 어떻게 고를건지 ->  A,B 어떻게 섞어서 바꿀 건지

        // 현재 막 선택, A로 바꿀 경우
        int[] original = film[row].clone();
        Arrays.fill(film[row],0);
        if(injectSimulate(row + 1, injectNum, useNum + 1)) {
            return true; // 성공 시 종료
        }

        // 현재 막 선택, B로 바꿀 경우

        Arrays.fill(film[row],1);
        if(injectSimulate(row + 1, injectNum, useNum + 1)) {
            return true; // 성공 시 종료
        }

        film[row] = original;
        return false;
    }



    static public boolean checkFilm(int[][] film) {
        for(int c = 0; c < W; c++) {
            boolean columnPass = false;

            // 현재 열에서 연속된 구간 찾기
            int count = 1;
            for(int r = 1; r < D; r++) {
                if(film[r][c] == film[r-1][c]) {
                    count++;
                } else {
                    count = 1; // 연속이 끊어지면 1부터 다시 시작
                }

                if(count >= K) {
                    columnPass = true;
                    break;
                }
            }

            if(!columnPass) return false;
        }
        return true;
    }
//
//    static public boolean checkFilm(int[][] film) {
//        // 처음에 A개수, B개수 구해서 하려 했음 -> 연속되어야 하므로 틀린 방법
//
//        for(int c = 0; c < W; c++) {
//            boolean columnPass = false;
//            for(int r = 0; r <= D - K; r++) {
//                int count = 1;
//
//                if(K == 1) {
//                    columnPass = true;
//                    break;
//                }
//
//                for(int next = r + 1; next < D; next++) {
//                    if(film[r][c] == film[next][c]) {
//                        count++;
//                        if(count >= K) {
//                            columnPass = true;
//                            break;
//                        }
//                    } else {
//                        break;
//                    }
//                }
//                if(columnPass) break;
//            }
//            if(!columnPass) return false;
//        }
//        return true;
//    }



}
