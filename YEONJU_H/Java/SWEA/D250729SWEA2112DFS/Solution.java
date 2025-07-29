package D250729SWEA2112DFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

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
            - 이전 풀이를 DFS 방식으로 재풀이

        */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int t = 0;
        int usedMedicine;

        while (t++ < T) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            D = Integer.parseInt(st.nextToken()); // 두께
            W = Integer.parseInt(st.nextToken()); // 가로
            K = Integer.parseInt(st.nextToken());
            usedMedicine = 0;
            film = new int[D][W];
            minNum = 0;

            for(int r = 0; r < D; r++) {
                st = new StringTokenizer(br.readLine());
                for(int c = 0; c < W; c++) {
                    film[r][c] = Integer.parseInt(st.nextToken());
                }
            }

//            System.out.println(Arrays.deepToString(film));
            DFS(0, usedMedicine);

            System.out.println("#" + t + " " + minNum);
        }
    }


    static void DFS(int depth, int usedMedicine) {
        if (usedMedicine >= minNum) {
            return;
        }

        // 성능 검사 통과하면 최솟값 갱신
        if (checkFilm()) {
            minNum = Math.min(minNum, usedMedicine);
            return;
        }

        // 모든 막을 다 처리했으면 종료
        if (depth == D) {
            return;
        }

        // 현재 막 건드리지 않음
        DFS(depth, usedMedicine);

        int[] original = film[depth].clone();

        // 선택 2: A 약품 투입
        Arrays.fill(film[depth], 0);
        DFS(depth + 1, usedMedicine + 1);

        // 선택 3: B 약품 투입
        Arrays.fill(film[depth], 1);
        DFS(depth + 1, usedMedicine + 1);

        // 백트래킹: 원본 복원
        film[depth] = original;

    }

    static public boolean checkFilm() {
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

}
