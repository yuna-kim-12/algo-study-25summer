package D251007BJ20055;

import java.io.*;
import java.util.*;

public class MainLinkedList {
    static LinkedList<Integer> belt;
    static LinkedList<Boolean> robots;
//    static boolean[] robots;
    static int N,K;
    public static void main(String[] args) throws IOException {
        /*
            컨베이어 벨트 위의 로봇
            길이가 N인 컨베이어 벨트
            길이가 2N인 컨베이버 벨트가 위아래로 감쌈
            벨트는 길이 1간격으로 2N개의 칸으로 나뉘며 번호가 매겨져 있음

            올리는 위치 idx 0 / 내리는 위치 idx N-1
            컨베이어 벨트에 박스 모양 로봇을 하나씩 올림. 로봇은 올리는 위치에만 올릴 수 있음
            로봇이 내리는 위치에 도달하면 즉시 내림
            로봇은 컨베이어 벨트 위에서 스스로 이동 가능
            로봇을 올리는 위치에 올리거나, 로봇이 어떤 칸으로 이동하면 그 칸의 내구도 1 감소
            컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려함

            1. 벨트가 각 칸위에 있는 로봇과 함께 한칸 회전
            2. 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한 칸 이동 가능하면 이동 / 이동 불가 시 가만히
            3. 로봇이 이동하기 위해서는 해당 칸에 로봇이 없고, 내구도가 1이상 남아있어야 함
            4. 올리는 위치의 칸의 내구도가 0이 아닐 때 올리기 가능
            5. 내구도가 0인 칸의 개수가 K개가 되면 과정 종료 / 아니라면 1번으로 돌아감
            종료될 경우 몇 단계가 진행 중 이었는지 구해보기. 가장 처음 수행되는 단계는 1단계이다.

            [ 입력 ]
            첫째 줄에 N,K 가 주어진다. 둘째 줄에는 A1,A2... A2N 이 주어진다
            2 ≤ N ≤ 100
            1 ≤ K ≤ 2N
            1 ≤ Ai ≤ 1,000

            [ 출력 ]
            몇 번째 단계가 진행 중일 때 종료였는지 출력
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        belt = new LinkedList<>();
        robots = new LinkedList<>();

        // 초기화
        for(int i = 0; i < 2 * N; i++) {
            robots.add(false);
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < 2 * N; i++) {
            belt.add(Integer.parseInt(st.nextToken()));
        }


        int ans = 0;
        while(true) {
            // 3. 단계 증가
            ans++;

            // 1. 컨베이어 벨트와 로봇 이동
            rotateBelt();

            // 로봇 내리기
            if(robots.get(N-1)) {
                robots.set(N-1, false);
            }

            moveRobots();

            // 로봇 내리기
            if(robots.get(N-1)) {
                robots.set(N-1, false);
            }

            // 2. 로봇 올리기
            if(belt.get(0) > 0 && !robots.get(0)) {
                robots.set(0, true);
                belt.set(0, belt.get(0) -1); // 내구도 감소
            }

            // 4. 내구도 체크 (종료 조건)
            if(checkDurability() >= K) break;

        }

        System.out.println(ans);

    }

    public static int checkDurability() {
        int cnt = 0;
        for(int i = 0; i < 2 * N; i++) {
            if(belt.get(i) == 0) {
                cnt++;
            }
        }
        return cnt;
    }

    public static void rotateBelt() {
        int tmp = belt.removeLast();
        belt.addFirst(tmp);

        boolean tmpRobot = robots.removeLast();
        robots.addFirst(tmpRobot);
    }

    public static void moveRobots() {
        // 뒤에서부터 순회 (N-2부터 0까지, N-1은 내리는 위치라 별도 처리)
        for(int i = N-2; i >= 0; i--) {
            if(robots.get(i)) {  // 이 칸에 로봇이 있으면
                int next = i + 1;  // 다음 칸

                // 이동 조건: 다음 칸에 로봇 없고 && 내구도 1 이상
                if(!robots.get(next) && belt.get(next) >= 1) {
                    // 이동!
                    robots.set(i, false);  // 현재 칸에서 제거
                    robots.set(next, true);  // 다음 칸으로 이동
                    belt.set(next, belt.get(next) - 1);  // 내구도 감소
                }
            }
        }
    }

}
