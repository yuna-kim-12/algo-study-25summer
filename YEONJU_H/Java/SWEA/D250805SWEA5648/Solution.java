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
    static Queue<Atom> atoms;
    static int N;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    static int[][] map;
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
            1. 첫 시도
            1) 1초씩 마다 1만큼 원자들 이동 시키기
            2) 이동 후, 충돌된 원자들 체크
            - x,y 값이 둘다 같은 원자 체크
            - 방문체크하면서, 한 원자 기준으로 반복적으로 체크하며
              충돌 시에는 해당 원자값의 e를 더한다.
              충돌 후에는 해당 원자 제거
              -- 사분면 별로 충돌 로직 구현 필요
              서로 반대방향이면서 마주 볼 경우 / 상하좌우 0123
              1) 방향이 서로 반대인 것끼리 체크. (한 원자를 잡고, 상이면 하만 필터링해서 본다.)
              상 : 하인 원자들 중, x값이 같고, y값이 위쪽위치이면 충돌
              하 : 상인 원자들 중, x값이 같고, y값이 아래쪽위치이면 충돌
              좌 : 우인 원자들 중, y값이 같고, x값이 왼쪽위치이면 충돌
              우 : 좌인 원자들 중, y값이 같고, x값이 오른쪽위치이면 충돌

            3) 이 과정을 좌표값이 가장 큰 원자의 좌표값 기준 횟수만큼 반복
            충돌을 체크하는 과정이 시간복잡도 N^2 라서, 시간 초과 발생


            2. 두 번째 시도 : BFS 활용
            시간차를 두는 것이 아니라, 원자를 순차적으로 pop하고 이동시키고 넣음으로써
            순서대로 돌면서 충돌 확인하는 로직을 2차원 배열을 중개로 구현.
            시간 복잡도 N으로 효율성 Up.

         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int t = 0;

        while (t++ < T) {

            N = Integer.parseInt(br.readLine());
            atoms = new LinkedList<>();
            crachScore = 0;
            map = new int[4001][4001];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int x = (Integer.parseInt(st.nextToken()) + 1000) * 2;
                int y = (Integer.parseInt(st.nextToken()) + 1000) * 2;
                int dir = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                atoms.add(new Atom(x, y, dir, e));
                map[x][y] = e;
            }

            bfs();
            System.out.println("#" + t + " " + crachScore);
        }


    }

    public static void bfs() {
        // 모두 이동 시킴

        while(!atoms.isEmpty()) {
            Atom a = atoms.poll();
            if(map[a.x][a.y] != a.energy) { // 다른 원자와 충돌 확인
                crachScore += map[a.x][a.y];
                map[a.x][a.y] = 0;
                continue;
            }

            int nx = a.x + dx[a.dir];
            int ny = a.y + dy[a.dir];

            if(nx >= 0 && ny >= 0 && nx <= 4000 && ny <= 4000) {
                if (map[nx][ny] == 0) {
                    map[nx][ny] = a.energy;
                    atoms.add(new Atom(nx, ny, a.dir, a.energy));
                } else {
                    map[nx][ny] += a.energy;
                }
            }

            map[a.x][a.y] = 0;

        }

    }


}