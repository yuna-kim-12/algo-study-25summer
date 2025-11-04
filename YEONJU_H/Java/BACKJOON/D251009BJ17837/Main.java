package D251009BJ17837;

import java.io.*;
import java.util.*;

public class Main {
    static class Horse {
        int no, r, c, dir;

        Horse(int no, int r, int c, int dir) {
            this.no = no;
            this.r = r;
            this.c = c;
            this.dir = dir;
        }
    }

    static int N,K;
    static int[][] board;
    static ArrayList<Horse>[][] recordHorse;
    static ArrayList<Horse> horseList;
    static int[] dr = {0,0,-1,1}; // 우좌상하
    static int[] dc = {1,-1,0,0};
    public static void main(String[] args) throws IOException {

        /*
          새로운 게임 2

          N*N판
          사용하는 말의 개수 K
          말은 원판모양이고, 말 위에 다른 말 올리기 가능
          체스판은 흰,빨,파 중 하나로 색칠되어 있음
          게임은 체스판 위에 말 K개를 놓고 시작, 말은 1~K번까지 번호 매겨져 있고, 이동 방향(상하좌우)도 정해져 있음

          턴 한번은 1~K 말까지 순서대로 이동시키는 것
          한 말이 이동할 때 위로 올려져있는 말도 함께 이동
          말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같음
          말이 4개 이상 쌓이는 순간 게임 종료


            # A번 말이 이동하려는 칸이
            ## 흰색일 경우
            - 그 칸으로 이동 / 이미 말이 있는 경우 가장 위에 A번 말을 올려놓음
            - A번 말 위에 다른 말이 있는 경우 A번 말과 위에 있는 모든 말이 이동
            - 기존에 말이 있으면 그 위에 쌓임 (DE가 있을경우 ABC 가 이동하면, DEABC가 됨) //

            ## 빨간색인 경우
            - 이동 후 A번 말과 그 위에 있는 모들 말의 쌓여있는 순서를 반대로 바꿈
            - ABC가 이동하고 이동하려는 칸에 말이 없는 경우 CBA 가 됨
            - ADFG 가 이동하고 이동하려는 말칸에 말이 있는 경우 ECB GFDA 가 됨 (그 위에 반대로 쌓임)

            ## 파란색인 경우
            이동방향을 반대로 하고 한칸 이동
            방향을 바꾼 후에 이동하려는 칸이 파랑이면 이동하지 않음
            체스판을 벗어나는 경우에는 파란색과 같은 경우

           [ 입력 ]
           체스판 크기  4 ≤ N ≤ 12
           말 개수 4 ≤ K ≤ 10
           N개의 줄에 체스판 정보

           흰 0 / 빨 1 / 파 2
           K개 말의 정보가 1번 말부터 주어짐.
           말 정보는 3개의 정수 (행 / 열/ 이동방향)
           행 열의 번호는 1부터 시작, 이동방향은 1,2,3,4 (우,좌,상,하) 의미

           [ 출력 ]
            게임이 종료되는 턴의 번호 출력
            그 값이 1000보다 크거나 절대로 종료되지 않는 게임일 경우 -1 출력

           [ 풀이 설계 ]
           0. 시간 복잡도

            - 최악의 시간 복잡도
            체스판 크기 12*12
            말의 개수 10
            최대 턴 수 1000
            10*10*1000 말을 이동시키면서 종료조건을 체크할 때 최악의 경우 = 100000

           1. 풀이 설계
           - 말 정보를 클래스로 입력 받는다.
           - 입력 정보를 통해서 말을 이동시킨다.
              - 이동시킬 때마다 칸의 색깔을 판단한다
           - 모든 말이 한번씩 이동 했을때가 1턴
           - 말을 계속해서 이동시키면서 칸색 조건과 종료조건을 체크한다.
                - 칸색 조건

                - 종료 조건
                    4개 이상의 말이 쌓인 칸이 있는가
                    쌓임 체크를 위해서 2차원 배열 칸 별로 arrayList를 위치시켜야 할까?
                    queue를 이용해야할 것 같은 느낌인데
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        board = new int[N][N];
        recordHorse = new ArrayList[N][N];
        horseList = new ArrayList<>();

        for(int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for(int c = 0; c < N; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
                recordHorse[r][c] = new ArrayList<>();
            }
        }

        int hr,hc,hDir;
        for(int k = 0; k < K; k++ ) {
            st = new StringTokenizer(br.readLine());
            hr = Integer.parseInt(st.nextToken()) - 1;
            hc = Integer.parseInt(st.nextToken()) - 1;
            hDir = Integer.parseInt(st.nextToken()) - 1;

//            recordHorse[hr][hc].add(new Horse(k,hr,hc,hDir));
//            horseList.add(new Horse(k,hr,hc,hDir));

            Horse horse = new Horse(k, hr, hc, hDir);
            recordHorse[hr][hc].add(horse);
            horseList.add(horse);  // 같은 객체 참조
        }

        // 말 이동 시키기
        // - 턴 세기
        // - 칸 색상별로 이동 로직 달리하기
        int t = 0;
        boolean gameEnd = false;
        while(true) {
            t++; // 초기에 하나, 마지막에 하나 상관 없나?
            if(t > 1000) break;

            // 게임 종료 조건 체크
            if (moveHorses()) {
                gameEnd = true;
                break;
            }
        }

        if(t > 1000 || !gameEnd) {
            System.out.println(-1);
        } else {
            System.out.println(t);
        }

    }

    static boolean checkEnd() {
        for(int r = 0; r < N; r++) {
            for(int c = 0; c < N; c++) {
                if(recordHorse[r][c].size() >= 4) {
                    return true;
                }
            }
        }
        return false;
    }

    public static boolean moveHorses() {

        for(Horse h : horseList) {
            int nr = h.r + dr[h.dir];
            int nc = h.c + dc[h.dir];

            // 피랑이거나 벽일 경우, 방향 변경 후 한칸 더 이동
            if(nr < 0 || nc < 0 || nr >= N || nc >= N || board[nr][nc] == 2) {
                // 방향 반대로 바꾸고 한칸 더 이동 / 우좌상하 1234
                if (h.dir == 0) {
                    h.dir = 1;
                } else if (h.dir == 1) {
                    h.dir = 0;
                } else if (h.dir == 2) {
                    h.dir = 3;
                } else if (h.dir == 3) {
                    h.dir = 2;
                }
                // horseRecord Data 도 갱신
                nr = h.r + dr[h.dir];
                nc = h.c + dc[h.dir];

                // 또 범위 밖이거나 파란색이면 이동 안 함
                if(nr < 0 || nc < 0 || nr >= N || nc >= N || board[nr][nc] == 2) {
                    continue;
                }
            }

            // 새로운 칸으로 말 이동
            move(h.no, nr, nc, board[nr][nc] == 1);

            // 이동 후 즉시 종료 조건 체크
            if (recordHorse[nr][nc].size() >= 4) {
                return true;
            }
        }
        return false;
    }

    static boolean checkIsBlue( int nr, int nc) {
        if(board[nr][nc] == 3) return true;
        return false;
    }

    // 말 번호, 새롭게 갈 위치와 해당 위치가 Red 인지여부만 알려주면 말을 옮기는 로직
    static void move(int horseNo, int nr, int nc, boolean isRed) {
        Horse h = horseList.get(horseNo);
        int r = h.r;
        int c = h.c;

        // 현재 해당 칸에서 idx 찾기
        // int idx = recordHorse[r][c].indexOf(horseNum);
        int findIndex = -1;
        for(int i = 0; i < recordHorse[r][c].size(); i++) {
            if(recordHorse[r][c].get(i).no == horseNo) {
                findIndex = i;
//                recordHorse[r][c].get(i).dir = horse.dir;
                break;
            }
        }

        // 혹시나..
        if(findIndex == -1) return;

        // 움직일 말들을 담을 임시 배열
        List<Horse> movingHorses = new ArrayList<>();

        // 자신보다 뒤쪽 idx의 배열을 담음
        for(int i = findIndex; i < recordHorse[r][c].size(); i++) {
            movingHorses.add(recordHorse[r][c].get(i));
        }

        // 기존 위치의 말들을 삭제
        for(int i = recordHorse[r][c].size() - 1; i >= findIndex; i--) {
            recordHorse[r][c].remove(i);
        }

        // 빨간 칸일 경우, 옮길 말들의 순서를 꺼꾸로
        if(isRed) {
            Collections.reverse(movingHorses);
        }

        // 옮긴 말들의 정보를 갱신
        for(Horse horse  : movingHorses) {
            recordHorse[nr][nc].add(horse);
            horse.r = nr;
            horse.c = nc;
        }

    }
}
