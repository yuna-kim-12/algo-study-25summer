package D250901BJ15686;

import java.util.*;
import java.io.*;

public class Main {
    static int N,M;
    static int[][] map;
    static int[][] sel;
    static int minDis = Integer.MAX_VALUE;

    // 0 빈 칸, 1 집, 2 치킨집
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        sel = new int[M][2];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        ArrayList<int[]> houses = new ArrayList<>();
        ArrayList<int[]> stores = new ArrayList<>();


        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(map[i][j] == 1) {
                    houses.add(new int[] {i,j});
                } else if(map[i][j] == 2) {
                    stores.add(new int[] {i,j});
                }
            }
        }

        // List 내부의 치킨집 중 M개 고르기
        // M개 고른 조합들을 2차원 배열로 받기
        combi(0, 0, stores, houses);


        System.out.println(minDis);
    }

    private static void combi(int sIdx, int idx, ArrayList<int[]> stores, ArrayList<int[]> houses) {
        if(sIdx == M) {
            calculateDis(houses);
            return;
        }

        // M개를 선택하지 못한 경우
        if(idx == stores.size()) {
            return;
        }

        // 지금 집을 골랐을 경우
        sel[sIdx] = stores.get(idx);
        combi( sIdx+1,idx + 1, stores, houses);

        // 안골랐을 경우
        combi( sIdx, idx + 1,stores, houses);

    }

    private static void calculateDis(ArrayList<int[]> houses) {
        int sum = 0;

        for(int i = 0; i < houses.size(); i ++) { // houses
            int min = Integer.MAX_VALUE;
            for(int j = 0 ; j < M; j ++) {
                int dis = Integer.MAX_VALUE;
                int[] a = houses.get(i);
                int[] b = sel[j];
                dis = Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
                min = Math.min(min, dis);
            }
            sum = sum + min;
        }

        minDis = Math.min(minDis, sum);
    }


}