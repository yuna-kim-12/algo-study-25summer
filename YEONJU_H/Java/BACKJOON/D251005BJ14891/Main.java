package D251005BJ14891;

import java.io.*;
import java.util.*;
public class Main {
    static LinkedList<Integer>[] gears;
    public static void main(String[] args) throws IOException{
        /*
            톱니바퀴

            8개의 톱니가진 4개의 바퀴 1,2,3,4
            회전횟수 1 <= K <= 100
            12시방향부터 시계방향순으로 상태 주어짐
            같은 극끼리 만나면 회전 안함
            움직인 바퀴와 다른 극일 경우 반대방향으로 회전
            N극 0, S극 1
            시계방향 1, 반시계 방향 -1

            [ 출력 ]
            1번 : 12시 방향이 N-0 S-1
            2번 : N-0 / S-2
            3번 : N-0 / S-4
            4번 : N-0 / S-8

            점수 합산하여 출력

            [ 아이디어 ]
            1-2 : idx 2, idx 6
            2-3 : idx 2, idx 6
            3-4 : idx 2, idx 6

            단순 구현
            바퀴의 회전을 어떻게 반영할 것인가?
            삽입삭제를 원활하게 하기 위해서는 각각 연결리스트로 받기
            ArrayList 와 LinkedList 비교
            
         */


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        gears = new LinkedList[4];

        for(int i = 0; i < 4; i++) {
            gears[i] = new LinkedList<>();
            String tmp = br.readLine();
            for(int j = 0; j < 8; j++) {
                gears[i].add(tmp.charAt(j) - '0');
            }
        }

        int K = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int gearNo, dir;
        int[] rotations ;
        // true 시계 / false 반시계
        for(int k = 0; k < K; k++) {
            st = new StringTokenizer(br.readLine());
            gearNo = Integer.parseInt(st.nextToken()) - 1;
            dir = Integer.parseInt(st.nextToken());
            // 현재 기어 돌리기
            rotations = new int[4];
            rotations[gearNo] = dir;

            for(int i = gearNo; i < 3; i++) {
                if(gears[i].get(2) != gears[i+1].get(6)) {
                    rotations[i+1] = -rotations[i];
                } else {
                    break;
                }
            }

            for(int i = gearNo; i > 0 ; i--) {
                if(gears[i].get(6) != gears[i-1].get(2)) {
                    rotations[i-1] = -rotations[i];
                } else {
                    break;
                }
            }

            for(int i = 0; i < 4; i++) {
                if(rotations[i] == 1) { // 시계방향일경우
                    rotate(i);
                } else if(rotations[i] == -1) { // 반시계
                    rotateReverse(i);
                } // 아무것도 아닐 땐 아무일도
            }

        }

        int ans = 0;
        for(int k = 0; k < 4; k++) {
            switch(k) {
                case 0:
                    if(gears[k].get(0) == 1) {
                        ans += 1;
                    }
                    break;
                case 1:
                    if(gears[k].get(0) == 1) {
                        ans += 2;
                    }
                    break;

                case 2:
                    if(gears[k].get(0) == 1) {
                        ans += 4;
                    }
                    break;
                case 3:
                    if(gears[k].get(0) == 1) {
                        ans += 8;
                    }
                    break;
            }
        }
        System.out.println(ans);
    }

    public static void rotate(int gearNo) {
        LinkedList<Integer> gear = gears[gearNo];
        int last = gear.removeLast();
        gear.addFirst(last);
    }

    public static void rotateReverse(int gearNo) {
        LinkedList<Integer> gear = gears[gearNo];
        int first = gear.removeFirst();
        gear.addLast(first);
    }

}
