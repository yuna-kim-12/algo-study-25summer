package D251007BJ20055;

import java.io.*;
import java.util.*;

public class Main {
    static int[] belt;
    static boolean[] robots;
    static int N, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        belt = new int[2 * N];
        robots = new boolean[2 * N];  // 자동으로 false로 초기화됨

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < 2 * N; i++) {
            belt[i] = Integer.parseInt(st.nextToken());
        }

        int ans = 0;
        while(true) {
            ans++;

            // 1. 벨트와 로봇 회전
            rotateBelt();

            // 로봇 내리기
            if(robots[N-1]) {
                robots[N-1] = false;
            }

            // 2. 로봇 이동
            moveRobots();

            // 로봇 내리기
            if(robots[N-1]) {
                robots[N-1] = false;
            }

            // 3. 로봇 올리기
            if(belt[0] > 0 && !robots[0]) {
                robots[0] = true;
                belt[0]--;
            }

            // 4. 종료 조건
            if(checkDurability() >= K) break;
        }

        System.out.println(ans);
    }

    public static int checkDurability() {
        int cnt = 0;
        for(int i = 0; i < 2 * N; i++) {
            if(belt[i] == 0) cnt++;
        }
        return cnt;
    }

    public static void rotateBelt() {
        // 벨트 회전
        int tmpBelt = belt[2 * N - 1];
        for(int i = 2 * N - 1; i > 0; i--) {
            belt[i] = belt[i - 1];
        }
        belt[0] = tmpBelt;

        // 로봇 회전
        boolean tmpRobot = robots[2 * N - 1];
        for(int i = 2 * N - 1; i > 0; i--) {
            robots[i] = robots[i - 1];
        }
        robots[0] = tmpRobot;
    }

    public static void moveRobots() {
        for(int i = N - 2; i >= 0; i--) {
            if(robots[i]) {
                int next = i + 1;
                if(!robots[next] && belt[next] >= 1) {
                    robots[i] = false;
                    robots[next] = true;
                    belt[next]--;
                }
            }
        }
    }
}