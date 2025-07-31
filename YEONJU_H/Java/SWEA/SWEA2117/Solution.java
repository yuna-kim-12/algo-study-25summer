package SWEA2117;

import java.io.*;
import java.util.*;
import java.lang.Math;

class Solution {
    public static void main(String[] args) throws IOException {
        /*
            - N*N 크기의 도시에 홈방법 서비스를 제공하려고 한다.
            - 홈방법 서비스는 운영 상의 이유로 마름모 형태로만 제공
            - 홈방범 서비스 제공을 위해 운영 비용 필요
            - 서비스 영역의 크기 K가 커질수록 운용 비용이 커짐
            - 운영 비용은 서비스 영역의 면적과 동일하고, 아래와 같이 구할 수 있음
            - 운영 비용 = K*K + (K-1) * (K-1)
            - 운영 영역의 크기 K = 1이상의 정수
            - 도시를 벗어난 영역에 서비스를 제공하더라도 운영 비용 변경은 없음

            [ 주어지는 정보 ]
            N = 도시의 크기, M = 하나의 집이 지불할 수 있는 비용, 도시 정보

            서비스 운영비용 = 서비스 영역 면적과 동일
            5 <= N <= 20
            1 <= M <= 10
            최소 한 개 이상의 집 존재 /
            집 1 / 나머지 0

            [ return ]
            손해를 보지 않으면서 홈 방범 서비스를 가장 많은 집들에 제공하는 서비스 영역 찾고,
            홈 방법 서비스를 제공받는 집들의 수를 출력

            [ 아이디어 ]
            1) 한 칸씩 움직여 가면서, K 만큼씩 마름모 형태로 움직이며 그 안에 있는 집 파악하기 (최대 수 갱신하면서)
            - 한 칸 중심으로 아래나 위로갈 수록 좌우 한칸 씩 덜 움직이기
            2) K 감소 (가장 최대의 K 부터 --)
            3) K의 최대 숫자마다 서비스 운영 비용 계산하기
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        int t = 0;
        while(t++ < T){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken()); // 도시 크기
            int M = Integer.parseInt(st.nextToken()); // 하나의 집이 지불 가능한 비용

//            System.out.println("T,N,M" + " " + T + " " +  N + " " + M);

            int[][] map = new int[N][N];
            for(int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int maxServiceCount = 0;
            // K는 현재 마름모의 크기
            for(int K = 2 * N; K > 0; K--) {
                int total = 0;
                int cost = K * K + (K - 1) * (K - 1);
                int maxHouseCount = 0; // K 크기 마름모에서의 maxHounse 수
                for(int i = 0; i < N; i++) {
                    for(int j = 0; j < N; j++) {
                        int HouseCount = 0;
                        for(int x = 0; x < N; x++) {
                            for(int y = 0; y < N; y++){
                                int dist = Math.abs(x - i) + Math.abs(y - j);
                                if(dist < K) {
                                    HouseCount += map[x][y];
                                }
                            }
                        }

                        if(HouseCount > maxHouseCount) {
                            maxHouseCount = HouseCount;
                        }
                    }
                }
                total = maxHouseCount * M - cost;
                // total 이 음수, 항상 손해일 경우는 없나? 집이 하나일 때, K =1 이면 비용이 1, M이 1이면 손해는 아님
                if(total >= 0 && maxHouseCount > maxServiceCount  ) {
                    maxServiceCount = maxHouseCount;
                }
            }


            System.out.println("#" + t + " " + maxServiceCount);
        } // while

    }
}