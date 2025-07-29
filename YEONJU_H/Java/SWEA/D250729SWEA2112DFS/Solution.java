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
            minNum = Integer.MAX_VALUE;

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
        DFS(depth + 1, usedMedicine);

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
