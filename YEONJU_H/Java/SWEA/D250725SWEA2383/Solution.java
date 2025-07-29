package D250725SWEA2383;
import java.util.*;
import java.io.*;

class Person {
    int r,c,sr,sc,dis,sk;
    Person(int r, int c) {
        this.r = r;
        this.c = c;
    }

    public void setStairs(int sr, int sc, int sk) {
        this.sr = sr;
        this.sc = sc;
        this.dis = Math.abs(r - sr) + Math.abs(c - sc);
        this.sk = sk;
    }

    @Override
    public String toString() {
        return "Person{pos=(" + r + "," + c + "), stair=(" + sr + "," + sc + "), dis=" + dis + ", sk=" + sk + "}";
    }

}

class Stair {
    int sr,sc,k,pNum;
    Stair(int sr, int sc, int k) {
        this.sr = sr;
        this.sc = sc;
        this.k = k;
        pNum = 0;
    }
}

class Solution {

    static ArrayList<Person> persons = new ArrayList<>(10);
    static ArrayList<Stair> stairs = new ArrayList<>(2);
    static int N, minTime;
    public static void main(String[] args) throws Exception {
        /*
            https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
            N*N 크기의 정사각형 모양의 방에 사람들이 앉아 있음.
            점심을 먹기 위해 아래 층으로 내려가야 하는데, 밥을 빨리 먹기위해 최대한 빠른 시간 내에 내려가야
            - P : 방 안의 사람
            - S : 계단 입구

            이동 완료 시간 = 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료한 시간
            사람들이 아래층으로 이동하는 시간은 계단 입구까지 이동 시간과 계단을 내려가는 시간이 포함됨

            계단 입구까지 이동 시간
            : 사람이 현재 위치에서 계단 입구까지 이동하는데 걸리는 시간
            이동시간 = | PR - SR | + | PC - SC |
            PR, PC : 사람 P의 세로,가로 위치 / SR, SC = 계단 입구 S의 세로 위치, 가로 위치

            계단 내려가는 시간
            - 계단 입구 도착 후 계단을 완전히 내려가는 시간
            - 계단 입구 도착 시, 1분 후 아래칸으로 내려갈 수 있음
            - 계단 위는 최대 3명까지 올라갈 수 있음
            - 이미 3명이 계단을 내려가고 있는 경우, 그 중 한명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 함
            - 계단마다 길이 K가 주어지고, 계단에 올라간 후 완전히 내려가는데 K 분 소요

            [ 구해야 할 것 ]
            모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우 찾기
            이 때, 소요 시간을 출력하는 프로그램 작성

            [ IDEA ]
            0) 사람 노드와 계단 노드 각각 필요
            (1) 사람 노드 : 현 위치, 가장 가까운 계단의 위치, 계단까지의 거리
            (2) 계단 노드 : 계단의 길이, 현재 계단을 내려가고 있는 사람 수
            - 조건 : 최대 3명
            - 계단 길이 : K / 계단 내려갈 때 K 분 소요

            1) 각각의 사람, 가장 가까운 계단 찾기
            (1) 1분씩 이동하면서, 그 방향으로 움직이는 로직 넣기

            2) 전반적인 방법
            - 1분마다 사람을 이동시키고, 계단의 상태를 변화시키면서 사람을 내려보낸다.
            - 이때 계단에 올라가는 사람의 순서는 상관 없다.
            - 소요 시간을 count 하는 static 변수 지정
            - 계단이 최대 2가지 이므로, 사람별로 ^2 개로 나눈다. 계단 길이가 변수가 될 수 있음.
            - 사람과 계단의 정보를 입력하는 로직, 사람을 나누는 로직, 1분마다 처리 로직,
         */

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st;


            int T = Integer.parseInt(br.readLine());
            int t = 0;

            while(t++ < T) {
                persons.clear();
                stairs.clear();
                minTime = Integer.MAX_VALUE;

                N = Integer.parseInt(br.readLine());
                int[][] map = new int[N][N];

                for(int i = 0; i < N; i++) {
                    st = new StringTokenizer(br.readLine());
                    for(int j = 0; j < N; j++) {
                        map[i][j] = Integer.parseInt(st.nextToken());
                        if(map[i][j] == 1) {
                            persons.add(new Person(i,j));
                        } else if( map[i][j] > 1) {
                            stairs.add(new Stair(i,j,map[i][j]));
                        }
                    }
                }

                // System.out.println(Arrays.deepToString(map));
                // 입력 완료

                // combi
                combi(0);
                System.out.println("#" + t + " " + minTime);
            }


    }

    public static void combi(int p) {

        if( p == persons.size()) {
            simulate();
            return;
        }


        persons.get(p).setStairs(stairs.get(0).sr, stairs.get(0).sc, stairs.get(0).k);
        combi(p + 1);

        persons.get(p).setStairs(stairs.get(1).sr, stairs.get(1).sc, stairs.get(1).k);
        combi(p + 1);
    }

    public static void simulate() {
        // ##### 중요 ! 복사해서 사용해야, sk 값이 꼬이지 않는다 !!!!
        List<Person> copyPersons = new ArrayList<>();
        for (Person p : persons) {
            Person cp = new Person(p.r, p.c);
            cp.setStairs(p.sr, p.sc, p.sk);  // 복사해서 동일한 계단 정보 넣기
            copyPersons.add(cp);
        }

        List<Person> stairOne = new ArrayList<>();
        List<Person> stairTwo = new ArrayList<>();

        for(Person p : copyPersons) {
            if(p.sr == stairs.get(0).sr && p.sc == stairs.get(0).sc ) {
                stairOne.add(p);
            } else {
                stairTwo.add(p);
            }
        }

        int stairOneTime = simulateStair(stairOne);
        int stairTwoTime = simulateStair(stairTwo);

        minTime = Math.min(minTime, Math.max(stairOneTime, stairTwoTime));
    }


    public static int simulateStair(List<Person> stairPersons) {
        List<Person> onStair = new ArrayList<>();  // 계단 이용 중 (최대 3명)
        int time = 0;
        if(stairPersons.isEmpty()) {
            return 0;  // 바로 0 반환
        }
        while(true) {
            time++;

            for(int i = onStair.size() - 1; i >= 0; i--) {
                if(onStair.get(i).sk > 0) {
                    onStair.get(i).sk--;
                }
                if(onStair.get(i).sk == 0) {
                    onStair.remove(i);
                }
            }

            // 2. 도착한 사람들 중 계단에 들어갈 수 있는 사람 추가
            for(int i = stairPersons.size() - 1; i >= 0; i--) {
                if(stairPersons.get(i).dis + 1 <= time && onStair.size() < 3) {
                    onStair.add(stairPersons.get(i));
                    stairPersons.remove(i);
                }
            }

            if(stairPersons.isEmpty() && onStair.isEmpty()) {
                return time;
            }
        }

    }
}