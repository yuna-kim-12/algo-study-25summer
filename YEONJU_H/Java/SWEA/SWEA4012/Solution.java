package SWEA4012;
import java.util.*;
import java.io.*;

public class Solution {
    static int N, R;
    static boolean[] selA;
    static int[][] foodScore;
    static int minDiff;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for(int t = 1; t <= T; t++) {
            N = Integer.parseInt(br.readLine());
            R = N/2;
            minDiff = Integer.MAX_VALUE;
            foodScore = new int[N][N];
            selA = new boolean[N];

            for(int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j = 0; j < N; j++) {
                    foodScore[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            combi(0, 0);

            System.out.println("#" + t + " " + minDiff);
        }
    }

    public static void combi(int idx, int sIdx) {
        if(sIdx == R) {
            int foodAscore = 0;
            int foodBscore = 0;

            // 팀 A 시너지 계산
            for(int i = 0; i < N; i++) {
                if(selA[i]) {
                    for(int j = 0; j < N; j++) {
                        if(selA[j] && i != j) {
                            foodAscore += foodScore[i][j];
                        }
                    }
                }
            }

            // 팀 B 시너지 계산
            for(int i = 0; i < N; i++) {
                if(!selA[i]) {
                    for(int j = 0; j < N; j++) {
                        if(!selA[j] && i != j) {
                            foodBscore += foodScore[i][j];
                        }
                    }
                }
            }

            int diff = Math.abs(foodAscore - foodBscore);
            minDiff = Math.min(diff, minDiff);

            return;
        }

        if(idx == N) {
            return;
        }

        // 현재 인덱스 선택
        selA[idx] = true;
        combi(idx + 1, sIdx + 1);

        // 현재 인덱스 선택하지 않음
        selA[idx] = false;
        combi(idx + 1, sIdx);
    }
}