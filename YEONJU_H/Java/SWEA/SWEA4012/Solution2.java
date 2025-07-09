import java.util.*;
import java.io.*;

// 틀린 로직 풀이 - 조합 boolean으로 설정하고 진행했어야 했는데, 잘못 생각했다.
public class Solution {

    static int N,R;
    static int[] foods;
    static boolean[] selA;
    static int total;
    static int[][] foodScore;
    static int minDiff;
    public static void main(String[] args) throws IOException{

        /*
            두 명의 손님에게 음식을 제공하려고 한다.
            둘에게 제공되는 음식은 최대한 비슷한 음식이어야 함
            N개의 식재료가 있고,
            식재료들을 N/2 개씩 나누어
            두 개의 요리를 하려고 한다. (N은 짝수)
            각각의 음식을 A,B 라고 했을 때

            식재료 같이 요리하게 될 경우 궁합이 잘 맞아 시너지 Sij가 발생
            각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij 들의 합

            식재료 i, j와 같이 요리하게 될 경우 발생하는
            시너지 Sij의 정보가 주어지고,

            [ 출력 ]
            가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때,
            두 음식간의 맛의 차이가 최소가 되는 경우를 찾고
            그 최솟값을 정답으로 출력하는 프로그램 작성

            [ 아이디어 ]
            두 음식에 대한 N/2가지 조합을 뽑으면서,A,B의 맛차이의 최솟값 찾기
            1) 한 음식에 대한 N/2가지 조합 찾기
            - N/2가지 조합에 대한 나머지 조합으로 나머지 음식 조합하기
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        int t = 0;

        while(t++ < T) {
            N = Integer.parseInt(br.readLine());
            R = N/2;
            minDiff = Integer.MAX_VALUE;
            foodScore = new int[N][N];
            selA = new boolean[N];
            total = 0;

            foods = new int[N];
            for(int i = 0; i < N; i++){
                foods[i] = i;
            }

            for(int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j = 0; j < N; j++) {
                    foodScore[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for(int i = 0; i < foodScore.length; i++) {
                for(int j = 0; j < foodScore.length; j++) {
                    if(i != j) {
                        total += foodScore[i][j];
                    }
                }
            }

            combi(0,0);

            System.out.println("#" + t + " " + minDiff);
        }
    }

    public static void combi(int idx,int sIdx) {
        if(sIdx == R ) { // 헷갈림 주의 ! sIdx 증가 후에 오는 자리이므로, (R = 2 일 때, idx = 0 반영하고 들어옴) R 이 맞음

            int foodAscore = 0;
            int foodBscore = 0;

            boolean[] selectedB = new boolean[N];
            int[] selB = new int[R];
            int a = 0;
            for(int i = 0; i < N; i++) {
                if(selA[a] != i) {
                    selectedB[selA[i]] = false;
                }

            }

            /* selA = {0,1};
                i = 0 j = 0 selA[0] = 0; {f,f,f,f}
                i = 0 j = 1 selA[1] = 1; {t,f,f,f}
                i = 1 j = 0 selA[0] = 0; {t,t,f,f}
                i = 1 j = 1 selA[1] = 1; {t,t,f,f}

                selA[1] = 1;


             */

            int bIdx = 0;
            for(int i = 0; i < N; i++) {
                if(selectedB[i]) {
                    selB[bIdx] = i;
                    bIdx++;
                }
            }


            for(int s1 : selA) {
                for(int s2 : selA ) {
                    if(s1 != s2) {
                        foodAscore += foodScore[s1][s2];
                    }
                }
            }

            for(int s1 : selB) {
                for(int s2 : selB ) {
                    if(s1 != s2) {
                        foodBscore += foodScore[s1][s2];
                    }
                }
            }

            System.out.println("selA: " + Arrays.toString(selA));
            System.out.println("selB: " + Arrays.toString(selB));


            int diff = Math.abs(foodAscore - foodBscore);
            minDiff = Math.min(diff, minDiff);
            System.out.println("foodAscore / foodBscore : " + foodAscore + "/" + foodBscore);


            return;
        }

        if(idx == N) {
            return;
        }

        // 재귀 부분 - 선택
        System.out.println("sIdx :" + sIdx + "/ idx : " + idx);
        selA[sIdx] = foods[idx];
        combi(idx + 1, sIdx + 1);
        // 미선택
        combi(idx + 1, sIdx);
    };


}