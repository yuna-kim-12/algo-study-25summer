package D250812SWEA2382;

import java.util.*;
import java.io.*;

class Mic {
    int r,c,nums,dir;
    Mic(int r, int c, int nums, int dir) {
        this.r = r;
        this.c = c;
        this.nums = nums;
        this.dir = dir;
    }
}

public class Solution {

    static int N,M,K;
    static List<Mic> mics;
    static int[] dr = {0,-1,1,0,0};
    static int[] dc = {0,0,0,-1,1};
    public static void main(String[] args) throws IOException{
        /*
            # 문제 요약
            - 가로 N, 세로 N
            - 가장 바깥쪽 = 특수 약품 칠해짐
            - 미생물 상하좌우 이동 (1,2,3,4)
            - 1시간마다 이동방향에 있는 다음셀로 이동
            - 약품 셀에 닿으면 군집 절반 죽음
                : 미생물이 홀수일 경우에는 소수점이하 버림
            - 군집 미생물이 한 마리 있는 경우 군집이 사라지게 됨
            - 이동 후 2개 이상 군집 한 셀이 모일 경우 군집 합쳐지고, 더 큰 군집의 방향으로 이동
            ( 같은 군집의 미생물 수는 주어지지 않으므로 고려하지 않아도 됨 )

            # 출력
            M시간 후 남아있는 미생물 수의 총합

            # 아이디어
            구현해야할 조건
            - 1시간마다 이동방향에 있는 다음셀로 이동
            - 약품 셀에 닿으면 군집 절반 죽음 : 미생물이 홀수일 경우에는 소수점이하 버림
            - 군집 미생물이 한 마리 있는 경우 군집이 사라지게 됨
            - 이동 후 2개 이상 군집 한 셀이 모일 경우 군집 합쳐지고, 더 큰 군집의 방향으로 이동
            ( 같은 군집의 미생물 수는 주어지지 않으므로 고려하지 않아도 됨 )

            미생물 상태를 map에 표시하는 게 나을까? 아니면 node 형태로 가져가는게 나을까?
            - 일단 둘다 가져가 보자 : BFS로 순차적으로 이동? 아니면 1초마다 증가시키면서 이동?
            - BFS로 이동할 경우 map이 필요하다.
            결론 => ArrayList로 구현하되, 겹치는 위치 체크를 sort를 활용해 인접만 체크되도록 한다.
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int t = 0;


        while(t++ < T) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken()); // map 크기
            M = Integer.parseInt(st.nextToken()); // 군집 방치 시간
            K = Integer.parseInt(st.nextToken()); // 미생물 군집 수

            mics = new ArrayList<>();

            for(int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int nums = Integer.parseInt(st.nextToken());
                int dir = Integer.parseInt(st.nextToken());
                mics.add(new Mic(r,c,nums,dir));
            }
            int m = 0;
            while(m++ < M) {
                // 미생물 일제히 이동
                moveMics();
                // 약품에 닿았는지 체크 및 처리
                isDrugContact();
                // 미생물 수 nums가 1과 같거나 작을 경우 0처리
                isDied();
                // sort 후 같은 위치 미생물들 체크하면서 합칠 것 합치기
                checkMerge();
            }

            int ans = 0;
            for(Mic mic : mics) {
                ans += mic.nums;
            }

            System.out.println("#" + t + " " + ans);

        }

    }
    public static void moveMics() {

        for(Mic mic : mics) {
            int nr = mic.r + dr[mic.dir];
            int nc = mic.c + dc[mic.dir];

            if(nr >= 0 && nc >= 0 && nr < N && nc < N) {
                mic.r = nr;
                mic.c = nc;
            }
        }

    }

    public static void isDrugContact() {
        for(int i = mics.size() - 1; i >= 0; i--) {
            Mic mic = mics.get(i);
            // 경계선에 있을 경우
            if(mic.r == 0 || mic.c == 0 || mic.r == N - 1 || mic.c == N - 1) {
                int tmp = mic.nums;
                mic.nums = (int) tmp / 2;
//                System.out.println("tmp : " + tmp + " " + "mic.nums" + " " + mic.nums);

                int tmp2 = mic.dir;
                switch(tmp2) {
                    case 1 :
                        mic.dir = 2;
                        break;
                    case 2 :
                        mic.dir = 1;
                        break;
                    case 3 :
                        mic.dir = 4;
                        break;
                    case 4 :
                        mic.dir = 3;
                        break;
                }
            }
        }
    }

    public static void isDied() {
        for(int i = mics.size() - 1; i >= 0; i--) {
            Mic mic = mics.get(i);
            if(mic.nums == 0) {
                mics.remove(i);
            }
        }
    }

    public static void checkMerge() {
        Collections.sort(mics, (a,b) -> {
            if(a.r == b.r) {
                if(a.c == b.c) return a.nums - b.nums;
                return a.c - b.c;
            }
            return a.r - b.r;
        });

        for(int i = mics.size() - 1; i >= 1; i--) {
            Mic m1 = mics.get(i);
            Mic m2 = mics.get(i - 1);

            if(m1.r == m2.r && m1.c == m2.c) {
                m2.dir = m1.dir;
                m2.nums += m1.nums;
                mics.remove(i);
            }
        }

    }


}
