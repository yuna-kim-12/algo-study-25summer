// 이 방법으로 풀면 테케 33개만 맞고 시초뜸 ㅜ BFS로 다시 풀기, 그리고 왜 BFS로 풀면 시초가 안뜨는지도 파악할 것
package D250805SWEA5648;

import java.io.*;
import java.util.*;

class Atom {
    int x, y, dir, energy;

    Atom(int x, int y, int dir, int energy) {
        this.x = x;
        this.y = y;
        this.dir = dir;
        this.energy = energy;
    }
}


public class Solution {
    static List<Atom> atoms;
    static int N;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {1,-1,0,0};
    static int crachScore;
    public static void main(String[] args) throws IOException {

        /*  문제 요약
            원자의 최초 위치 : x,y
            상하좌우 이동 가능
            모든 원자들의 이동속도 동일
            1초에 1만큼의 거리 이동
            최초 위치에서 동시에 이동 시작
            두 개 이상의 원자 동시 충돌 시, 충돌 완자들은 모두 보유한 에너지를 방출하고 소멸

            [ 출력 ] 원자들이 소멸되면서 방출하는 에너지의 총합
            - N은 1000개 이하
            - 원자들의 보유 에너지 K = 1이상 100이하
            - 원자들의 처음 위치 [x,y] 는 -1000이상 1000이하의 정수
            - 2차원 평면 위에서 움직이며 움직일 수 있는 좌표의 범위에 제한 없음
            - 이동방향 : 상 0, 하1, 좌2, 우3 으로 주어짐
            - 동시에 1초에 이동방향으로 1만큼 이동
            - 최초 위치는 서로 중복되지 않음
            - 2개 이상 원자 충돌 시 보유한 에너지 모두 방출, 소멸
            - 방향 바뀌지 않음 / 방출 에너지 주변 영향 안줌

            [ 아이디어 ]
            1) 1초씩 마다 1만큼 원자들 이동 시키기
            2) 이동 후, 충돌된 원자들 체크
            - x,y 값이 둘다 같은 원자 체크
            - 방문체크하면서, 한 원자 기준으로 반복적으로 체크하며
              충돌 시에는 해당 원자값의 e를 더한다.
              충돌 후에는 해당 원자 제거
              -- 사분면 별로 충돌 로직 구현 필요
              서로 반대방향이면서 마주 볼 경우 / 상하좌우 0123
              y,x /
              1) 방향이 서로 반대인 것끼리 체크. (한 원자를 잡고, 상이면 하만 필터링해서 본다.)
              상 : 하인 원자들 중, x값이 같고, y값이 위쪽위치이면 충돌
              하 : 상인 원자들 중, x값이 같고, y값이 아래쪽위치이면 충돌
              좌 : 우인 원자들 중, y값이 같고, x값이 왼쪽위치이면 충돌
              우 : 좌인 원자들 중, y값이 같고, x값이 오른쪽위치이면 충돌

            3) 이 과정을 좌표값이 가장 큰 원자의 좌표값 기준 횟수만큼 반복

         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int t = 0;

        while(t++ < T) {

            N = Integer.parseInt(br.readLine());
            atoms = new ArrayList<>();
            crachScore = 0;

            int maxVal = 0;

            for(int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken()) * 2;
                int y = Integer.parseInt(st.nextToken()) * 2;
                int dir = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                atoms.add(new Atom(x,y,dir,e));

                int curMaxVal = Math.max(Math.abs(x),Math.abs(y));
                if(curMaxVal > maxVal) {
                    maxVal = curMaxVal;
                }

            }

            int n = 0;
            while(n <= maxVal * 2 && !atoms.isEmpty()) {
                moveAtoms();
                checkCrash();
                n++;
                if(atoms.size() < 2) break;
            }

            System.out.println("#" + t + " " + crachScore);
        }


    }

    public static void moveAtoms() {
        // 모두 이동 시킴
        for( Atom a : atoms) {
            a.x += dx[a.dir];
            a.y += dy[a.dir];
        }
    }

    public static void checkCrash() {
        boolean[] crashed = new boolean[atoms.size()];

        // 충돌여부 일괄 체크
        for(int i = 0; i < atoms.size(); i++) {
            if(crashed[i]) continue; // i가 이미 check 된거면 pass
            Atom a1 = atoms.get(i);
            for(int j = i + 1; j < atoms.size(); j++) {
                Atom a2 = atoms.get(j);
//                switch(a1.dir) {
//                    case 0 :
//                        if(a2.dir == 1 && a1.x == a2.x && a1.y < a2.y) {
//                            crashed[i] = true;
//                            crashed[j] = true;
//                        }
//                        break;
//                    case 1:
//                        if(a2.dir == 0 && a1.x == a2.x && a1.y > a2.y) {
//                            crashed[i] = true;
//                            crashed[j] = true;
//                        }
//                        break;
//                    case 2:
//                        if(a2.dir == 3 && a1.y == a2.y && a1.x < a2.x) {
//                            crashed[i] = true;
//                            crashed[j] = true;
//                        }
//                        break;
//                    case 3:
//                        if(a2.dir == 2 && a1.y == a2.y && a1.x > a2.x) {
//                            crashed[i] = true;
//                            crashed[j] = true;
//                        }
//                        break;
//                }

                if(a1.x == a2.x && a1.y == a2.y && !crashed[j]) {
                    crashed[i] = true;
                    crashed[j] = true;
                }
            }
        }

        // 충돌된 원자 일괄 제거
        for(int i = atoms.size() - 1; i >= 0; i--) {
            if(crashed[i]) {
                crachScore += atoms.get(i).energy;
                atoms.remove(i);
            }
        }

    }

}
